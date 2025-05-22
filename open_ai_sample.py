import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv() # Loads Secret from .env file

token = os.getenv("SECRET") # Replace with your actual token
endpoint = "https://models.github.ai/inference"
model = "openai/gpt-4.1-nano"

client = OpenAI(
    base_url=endpoint,
    api_key=token,
)

print ("Welcome to OpenAI assistant, give me your question or type 'exit'\n to quit")
while True:
    question = input("Your question: ")
    if question.lower() == 'exit':
        print("Goodbye!")
        break
    response = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "Tu esi naudingas asistentas. Atsakyk visada lietuvių kalba.",
        },
        {
            "role": "user",
            "content": question,
        }
    ],
    temperature=1.0,
    top_p=1.0,
    model=model
)

    #try:
        #print("Assistant:", response.choices[0].message.content.strip())
    #except AttributeError:
        #print("Assistant:", response.choices[0].text.strip())    
    print(response.choices[0].message.content)
