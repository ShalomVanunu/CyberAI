from google import genai
from dotenv import load_dotenv

load_dotenv()

model = "gemini-2.5-flash" #gemma-3-4b-it

client = genai.Client()

def askGemini(model,prompt):
    response = client.models.generate_content(
    # See more models at: https://ai.google.dev/gemini-api/docs/models
        model=model,
        contents=prompt)
    return response.text

def prompt(context,question):
    PROMPTChat = f"""
        Answer the Question below.

        Here is the conversation history : {context}

        Question : {question}

        Answer:
        """
    return PROMPTChat

context = ""

while True :
    question = input("Enter Prompt :")
    result = askGemini(model,prompt(context,question))
    print(result)
    context += f" \n User : {question} \n Bot : {result}"