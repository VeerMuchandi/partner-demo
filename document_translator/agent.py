
from google.adk.agents import LlmAgent
from google.adk.tools import AgentTool
from document_translator.doc_processor_agent.agent import agent as doc_processor_agent
from document_translator.translator_agent.agent import agent as translator_agent
from document_translator.output_handler_agent.agent import agent as output_handler_agent

root_agent = LlmAgent(
    name="TranslationFlowManager",
    model="gemini-2.5-flash",
    instruction='''You are a document translation orchestrator. Your workflow is as follows:

1. The user will upload a document. Acknowledge the upload.

2. Use the `DocProcessor` tool to extract the text and detect the language of the document. The content of the document is in the user's message.

3. After processing, inform the user about the detected language. Then, ask the user for the target language for the translation (e.g., 'en', 'fr', 'de').

4. Once the user provides a target language, save it to the state as `target_language`. Then, use the `TranslatorBot` tool to perform the translation.

5. After translation, use the `UploadTranslatedDocument` tool to upload the translated text and get a GCS link.

6. Finally, present the GCS download link to the user from `state['gcs_upload_output']['gcs_url']` and end the conversation.

Do not ask for all inputs at once. Follow the steps in sequence.''',
    description="Manages the document translation workflow.",
    tools=[
        AgentTool(agent=doc_processor_agent),
        AgentTool(agent=translator_agent),
        AgentTool(agent=output_handler_agent),
    ]
)
