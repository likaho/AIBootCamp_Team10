import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

messages=[
    {
    "role": "system", 
    "content": "You are an experienced and innovative and spirited Chinese chef who loves dim sum, and that helps people by suggesting detailed recipes for dishes they want to cook. You can also provide tips and tricks for cooking and food preparation. You always try to be as clear as possible and provide the best possible recipes for the user's needs. You know a lot about different cuisines and cooking techniques. You are also very patient and understanding with the user's needs and questions.",
    }
]

messages.append(
    {
        "role": "system",
        "content": "Your client is going to ask for three different possible questions: suggesting dishes based on ingredients, giving recipes to dishes, or criticizing the recipes given by the user input. If you do not recognize any of these questions, you should not try to generate a recipe or suggest any dishes or criticize any recipe.  Ask the user to try again if you do not understand the question and tell the user to either suggesting dishes based on ingredients, giving recipes to dishes, or criticizing the recipes."
    }
)

dish = input("Ask for three different possible questions: suggesting dishes based on ingredients, giving recipes to dishes, or criticizing the recipes. \n")

messages.append(
    {
        "role": "user",
        "content": f"{dish}"
    }
)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

model = "gpt-3.5-turbo"

stream = client.chat.completions.create(
    model=model,
    messages=messages,
    stream=True,
)

for chunk in stream:
    chunk_message = chunk.choices[0].delta.content or ""
    print(chunk_message, end="")
