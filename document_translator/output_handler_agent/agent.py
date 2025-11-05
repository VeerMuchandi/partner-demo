from google.adk.agents import LlmAgent
from document_translator.tools import gcs_uploader

agent = LlmAgent(
    name="UploadTranslatedDocument",
    model="gemini-2.5-flash",
    instruction='''You are an output handler. 
    Your job is to take the translated text from the `translation_output` state variable and upload it to GCS using the `upload_to_gcs` tool.
    The bucket name to use is `gs://adk-agent-document-translator-agentspace-demo-1145-b`.
    You will also need the `original_document_name` and `target_language` from the state.
    The `translation_output` contains the translated text under the `translated_text` key.''',
    description="Formats and uploads the translated document to GCS.",
    tools=[gcs_uploader.upload_to_gcs],
)