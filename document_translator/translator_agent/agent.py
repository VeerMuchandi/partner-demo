
from google.adk.agents import LlmAgent
from document_translator.tools import translation_service

agent = LlmAgent(
    name="TranslatorBot",
    model="gemini-2.5-flash",
    instruction='''You are a translation agent. 
    Your job is to translate the text provided in the `document_processing_result` state variable from its source language to the target language provided in the `target_language` state variable. 
    Use the translate_text tool. The `document_processing_result` contains the text to be translated under the `text` key and the source language under the `lang` key.''',
    description="Translates text to a specified target language.",
    tools=[translation_service.translate_text],
)
