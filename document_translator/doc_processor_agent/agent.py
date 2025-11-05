from google.adk.agents import LlmAgent
from document_translator.tools import document_parser

agent = LlmAgent(
    name="DocProcessor",
    model="gemini-2.5-flash",
    instruction="You are a document processor. The user has provided document content. Your job is to take the document content from the conversation history and identify the language. Use the parse_document tool, passing the user's document content to the `document_content` parameter.",
    description="Extracts text and detects the language of a document.",
    tools=[document_parser.parse_document],
    output_key="document_processing_result"
)