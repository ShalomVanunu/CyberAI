from google import genai
from google.genai import types
import time
from dotenv import load_dotenv

load_dotenv()

client = genai.Client()

# File name will be visible in citations
##בפקודה הראשונה (create): אתה נותן שם למאגר (ה"מחסן"). אם קראת לו 'Takanon', זה השם של הקבוצה כולה.

file_search_store = client.file_search_stores.create(
    config=types.CreateFileSearchStoreConfig(display_name='Takanon')
)


operation = client.file_search_stores.upload_to_file_search_store(
  file='Takanon.pdf',
  file_search_store_name=file_search_store.name,
    config=types.UploadToFileSearchStoreConfig(display_name='file-Takanon')

)


while not operation.done:
    time.sleep(5)
    operation = client.operations.get(operation)

# הטענת קבצים
while True:
    prompt = input("Prompt")
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=f"{prompt}",
        config=types.GenerateContentConfig(
            tools=[
                types.Tool(
                    file_search=types.FileSearch(
                        file_search_store_names=[file_search_store.name]
                    )
                )
            ]
        )
    )

    print(response.text)