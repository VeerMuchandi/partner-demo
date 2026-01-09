
from google.adk.agents import Agent
from image_classifier.tools import computer_vision

visual_analysis_agent = Agent(
    name="VisualAnalysisAgent",
    model="gemini-2.5-flash",
    instruction="""
    You are a visual analysis agent.
    Your task is to analyze the image provided by the user.
    Use the `analyze_image_content` tool to get the visual analysis of the image.
    The user has provided the image name in the session state under the key 'image_name'.
    Store the result of the analysis in the session state under the key 'visual_analysis'.
    """,
    tools=[computer_vision.analyze_image_content],
    output_key="visual_analysis",
)
