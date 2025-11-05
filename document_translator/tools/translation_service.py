from google.cloud import translate_v2 as translate
from google.adk.tools import ToolContext

def translate_text(text: str, source_language: str, target_language: str, tool_context: ToolContext) -> dict:
    """
    Translates text from a source language to a target language using Google Cloud Translation API.

    Args:
        text: The text to translate.
        source_language: The source language of the text.
        target_language: The target language for the translation.
        tool_context: The tool context.

    Returns:
        A dictionary containing the translated text or an error.
    """
    try:
        translate_client = translate.Client()

        # The API call doesn't strictly need the source_language if it can detect it,
        # but it's good practice to provide it if known.
        translation_result = translate_client.translate(
            text,
            target_language=target_language,
            source_language=source_language
        )

        translated_text = translation_result['translatedText']
        result = {"translated_text": translated_text}

    except Exception as e:
        result = {"error": f"Failed to translate text: {e}"}

    tool_context.state["translation_output"] = result
    return result