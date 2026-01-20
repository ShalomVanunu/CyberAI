from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client()

response = client.models.generate_content(
# See more models at: https://ai.google.dev/gemini-api/docs/models
    model="gemini-2.0-flash-lite",
    contents="Explain  what is Electric CAR")

print(response.text)