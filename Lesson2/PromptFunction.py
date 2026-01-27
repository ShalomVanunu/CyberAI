from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()

#MODEL = "gemma-3-4b-it"
MODEL = "gemini-2.5-flash"
client = genai.Client()

def ask_gemini(request: str) -> str:
    response = client.models.generate_content(
        model=MODEL,
        contents=request,
        config=types.GenerateContentConfig(
            temperature=0.1)
        )
    return response.text
