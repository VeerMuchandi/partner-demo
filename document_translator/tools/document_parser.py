from google.adk.tools import ToolContext

def parse_document(document_content: str, tool_context: ToolContext) -> dict:
    """
    Parses document content to extract text and detect its language.
    For this mock, we just pass the content through and guess the language based on keywords.

    Args:
        document_content: The content of the document to parse.
        tool_context: The tool context.

    Returns:
        A dictionary containing the extracted text and the detected language.
    """
    text = document_content
    lang = "unknown"

    # Simple keyword-based language detection for mock purposes
    if "Este es un documento" in text:
        lang = "es"
    elif "Recette de coq au vin" in text:
        lang = "fr"
    elif "new study shows" in text:
        lang = "en"
    elif "Die neue Technologie" in text:
        lang = "de"
    elif "storia dell'arte italiana" in text:
        lang = "it"
    elif "Descubra as maravilhas" in text:
        lang = "pt"
    elif "De geschiedenis van Nederland" in text:
        lang = "nl"
    elif "Русская литература" in text:
        lang = "ru"
    elif "日本のビジネスマナー" in text:
        lang = "ja"
    elif "静夜思" in text:
        lang = "zh"
    else:
        # Default to English if no specific keywords are found
        lang = "en"

    return {"text": text, "lang": lang}