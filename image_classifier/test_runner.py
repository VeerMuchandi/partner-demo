import asyncio
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from image_classifier.agent import root_agent
from google.genai import types as genai_types

async def main():
    """Runs the agent with a sample query."""
    session_service = InMemorySessionService()
    await session_service.create_session(
        app_name="image_classifier", user_id="test_user", session_id="test_session"
    )
    runner = Runner(
        agent=root_agent, app_name="image_classifier", session_service=session_service
    )

    print("Starting agent with simulated image upload...")
    
    # Simulate uploading the file provided by the user
    image_path = "/usr/local/google/home/veermuchandi/.gemini/jetski/brain/b8c2ac6d-9921-453e-bb98-44b7204a55b4/uploaded_image_1767732779152.jpg"
    with open(image_path, "rb") as f:
        image_bytes = f.read()

    async for event in runner.run_async(
        user_id="test_user",
        session_id="test_session",
        new_message=genai_types.Content(
            role="user", 
            parts=[
                genai_types.Part.from_text(text="Classify this uploaded image."),
                genai_types.Part.from_bytes(data=image_bytes, mime_type="image/jpeg")
            ]
        ),
    ):
        if event.is_final_response():
            print(f"Agent: {event.content.parts[0].text}")

if __name__ == "__main__":
    asyncio.run(main())