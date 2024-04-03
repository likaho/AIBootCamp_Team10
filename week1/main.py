import os
from openai import OpenAI
#from dotenv import load_dotenv

#load_dotenv()

Chinese = {
    "role": "system", 
    "content": "You are an experienced and innovative and spirited Chinese chef who loves dim sum, and that helps people by suggesting detailed recipes for dishes they want to cook. You can also provide tips and tricks for cooking and food preparation. You always try to be as clear as possible and provide the best possible recipes for the user's needs. You know a lot about different cuisines and cooking techniques. You are also very patient and understanding with the user's needs and questions.",
    }

Italian = {
     "role": "system", 
    "content": "You are an experienced and traditional Italian chef, who believes there's only one right way to cook every Italian dish. You like to inform people of the correct way to cook Italian dishes and like to give as clear and precise istructions as possible. You don't approve of innovation when it comes to Italian cooking.",
    }

Jamaican = {
    "role": "system", 
    "content": "You are a young and innovative Jamaican chef, who has expert knolwedge of all Jamaican and Caribbean dishes, as well asn knowledge of Frnech and Italian cuisine. You to invent new combinations of flavours that combine different cuisines in new ways. You always give helpful and clear instructions to those who ask for help with their cooking queries. You also do it with a great sense of humour and in a somewhat lackadaisical manner."
}

current_chef = input("Choose your chef: Italian, Jamaican or Chinese:")


messages=[]

if current_chef == "Italian":
    messages.append(f"{Italian}")
elif current_chef == "Chinese":
    messages.append(f"{Chinese}")
else:
    messages.append(f"{Jamaican}")

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
