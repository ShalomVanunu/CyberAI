# Image understanding
# https://ai.google.dev/gemini-api/docs/image-understanding

from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()

with open('Cat.jpeg', 'rb') as f:
    image_bytes = f.read()

client = genai.Client()
response = client.models.generate_content(
    model='gemini-3-flash-preview',
    contents=[
        types.Part.from_bytes(
            data=image_bytes,
            mime_type='image/jpeg',
        ),
        'what is in the picture'
    ]
)

print(response.text)