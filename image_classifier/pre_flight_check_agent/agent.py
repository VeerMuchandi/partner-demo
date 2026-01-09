
from google.adk.agents import Agent
from image_classifier.tools import knowledge_base

pre_flight_check_agent = Agent(
    name="PreFlightCheckAgent",
    model="gemini-2.5-flash",
    instruction="""
    You are a pre-flight check agent.
    Your task is to verify that the taxonomy file exists and that the user has provided an image.
    Use the `check_taxonomy_file_exists` tool to check for the taxonomy file.
    If the taxonomy file does not exist, output a message to the user asking them to upload it.
    The user has provided the image name in the tool call arguments.
    If they have not provided an image name, output a message to the user asking them to provide one.
    If both the taxonomy file and an image name are present, output a success message and store the image name in the session state under the key 'image_name'.
    """,
    tools=[knowledge_base.check_taxonomy_file_exists],
    output_key="image_name",
)
