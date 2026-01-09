
from google.adk.agents import Agent

json_output_agent = Agent(
    name="JsonOutputAgent",
    model="gemini-2.5-flash",
    instruction="""
    You are a JSON output agent.
    Your task is to take the tagging results from the session state and format them into a single, structured, machine-readable JSON format.
    The tagging results are in the session state under the key 'tagging_results'.
    The image name is in the session state under the key 'image_name'.

    Structure the output as follows:
    "Image Name": {
        "Dimension Name": ["tag1", "tag2"],
        "Confidence": [score1, score2],
        "Rationale": "Your rationale here."
    }

    Ensure the final output is a single, valid JSON object.
    """,
    output_key="final_output",
)
