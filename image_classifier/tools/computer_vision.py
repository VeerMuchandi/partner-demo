
from typing import Optional
import os
import json
from google import genai
from .mock_data import get_mock_visual_analysis

def analyze_image_content(image_name: str, tool_context: Optional[dict] = None) -> dict:
    """Analyzes the content of an image and returns visual cues.
    
    If the image_name corresponds to a local file, it uses Gemini to analyze it.
    Otherwise, it checks the mock data.
    """
    # 1. Check for local file existence
    if os.path.exists(image_name):
        try:
            client = genai.Client(
                vertexai=True,
                project=os.environ.get("GOOGLE_CLOUD_PROJECT"),
                location=os.environ.get("GOOGLE_CLOUD_LOCATION", "us-central1")
            )
            
            with open(image_name, "rb") as f:
                image_bytes = f.read()
                
            prompt = """
            Analyze this image for a bank's marketing taxonomy.
            Return a purely JSON object with these keys:
            - "text": Any visible text in the image (string).
            - "backgroundColor": The dominant background color (string).
            - "objects": A list of visible objects (list of strings).
            
            Example output:
            {
                "text": "Bank of Future",
                "backgroundColor": "white",
                "objects": ["Man", "Laptop", "Coffee"]
            }
            """
            
            mime_type = "image/png" if image_name.lower().endswith(".png") else "image/jpeg"
            
            response = client.models.generate_content(
                model="gemini-2.0-flash-exp",
                contents=[
                    prompt,
                    genai.types.Part.from_bytes(data=image_bytes, mime_type=mime_type)
                ],
                config=genai.types.GenerateContentConfig(
                    response_mime_type="application/json"
                )
            )
            
            if response.text:
                return {"status": "success", "analysis": json.loads(response.text)}
            else:
                return {"status": "error", "message": "Gemini returned no response."}
                
        except Exception as e:
             return {"status": "error", "message": f"Gemini analysis failed: {str(e)}"}

    # 2. Fallback to Mock Data
    mock_analysis = get_mock_visual_analysis()
    if image_name in mock_analysis:
        return {"status": "success", "analysis": mock_analysis[image_name]}
    
    return {"status": "error", "message": f"No mock analysis found for {image_name} and file does not exist locally."}
