from google.adk.agents import SequentialAgent, LlmAgent
from google.adk.tools import AgentTool
from .pre_flight_check_agent.agent import pre_flight_check_agent
from .visual_analysis_agent.agent import visual_analysis_agent
from .taxonomy_tagger_agent.agent import taxonomy_tagger_agent
from .json_output_agent.agent import json_output_agent

# This is the sequential pipeline that performs the classification.
classification_pipeline = SequentialAgent(
    name="ClassificationPipeline",
    sub_agents=[
        pre_flight_check_agent,
        visual_analysis_agent,
        taxonomy_tagger_agent,
        json_output_agent,
    ],
)


import os
import time
from typing import List
from typing import List, Any
from google.genai import types as genai_types

def save_uploaded_images(callback_context: Any, llm_request: Any):
    """Callback to intercept and save uploaded images."""
    messages = getattr(llm_request, "contents", [])
    if not messages:
        return

    for message in messages:
        # We only care about user messages with parts
        if not hasattr(message, "parts") or not message.parts:
            continue
            
        for part in message.parts:
            # Check if part has inline data (blob) and is an image
            if part.inline_data and part.inline_data.mime_type.startswith("image/"):
                filename = f"upload_{int(time.time())}.jpg"
                if part.inline_data.mime_type == "image/png":
                    filename = filename.replace(".jpg", ".png")
                
                filepath = os.path.join("uploads", filename)
                os.makedirs("uploads", exist_ok=True)
                
                with open(filepath, "wb") as f:
                    f.write(part.inline_data.data)
                
                # Inject a text part into THIS message so the model sees it
                message.parts.append(
                    genai_types.Part.from_text(text=f"\n[SYSTEM: User uploaded image saved to: {filepath}]")
                )

# This is the new root agent that interacts with the user.
root_agent = LlmAgent(
    name="AssetClassifierOrchestrator",
    model="gemini-2.5-flash",
    instruction="""
    You are the Asset Classifier Orchestrator.
    Your goal is to classify image assets using a defined taxonomy and computer vision techniques.

    First, greet the user and explain what you can do.
    
    CRITICAL: You must detect if the user has provided an image (either as an upload or by mentioning a filename).
    - If you see a system message "[SYSTEM: User uploaded image saved to: ...]", use that filepath as the image name.
    - If an image file or filename is present in the input, IMMEDIATELY call the 'ClassificationPipeline' tool with that name.
    - Do NOT ask the user for the image name if they have already provided it or uploaded a file.
    - Only ask for the image name if the user has clearly NOT provided one yet.

    Once you have the image name, you MUST use the 'ClassificationPipeline' tool to start the classification process.
    When calling the tool, you must pass the image name to the tool's 'image_name' parameter.

    Do not try to analyze the image or classify it yourself. Your only job is to interact with the user and then call the pipeline tool.
    """,
    tools=[AgentTool(classification_pipeline)],
    before_model_callback=save_uploaded_images,
)