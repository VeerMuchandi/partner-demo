import asyncio
import os
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from document_translator.agent import root_agent
from google.genai import types as genai_types

async def main():
    """Runs the agent with a sample query simulating a file upload."""
    session_service = InMemorySessionService()
    session_id = "test_session_upload"
    await session_service.create_session(
        app_name="document_translator", user_id="test_user", session_id=session_id
    )
    runner = Runner(
        agent=root_agent, app_name="document_translator", session_service=session_service
    )

    # Simulate file content
    document_content = "Este es un documento para traducir."
    print(f"--- Simulating upload of document with content: '{document_content}' ---")

    # 1. First message: User provides the document content
    initial_message = genai_types.Content(
        role="user",
        parts=[genai_types.Part(text=document_content)]
    )

    print("\n--- User Query: [sends document] ---")
    async for event in runner.run_async(
        user_id="test_user",
        session_id=session_id,
        new_message=initial_message,
    ):
        if event.is_final_response() and event.content.parts[0].text:
            print(f"Agent Response: {event.content.parts[0].text}")

    # 2. Second message: User provides the target language
    target_language_message = genai_types.Content(
        role="user",
        parts=[genai_types.Part(text="en")]
    )
    
    print("\n--- User Query: en ---")
    async for event in runner.run_async(
        user_id="test_user",
        session_id=session_id,
        new_message=target_language_message,
    ):
        if event.is_final_response() and event.content.parts[0].text:
            print(f"Agent Response: {event.content.parts[0].text}")

if __name__ == "__main__":
    asyncio.run(main())