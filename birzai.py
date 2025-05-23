# # Create an AI application which would read information from file and would answer a question about Birzai.

# # 1. Load data as string from birzai.txt (u can change to your hometown)
# # 2. Setup openai client.
# # 3. Make a completion with openai client and pass the question and context in the completion.
# # 4. Print the answer.
import os
from openai import OpenAI
from dotenv import load_dotenv

with open('birzai.txt', 'r', encoding='utf-8') as f:
    birzai_text = f.read()
# print(f"Original text: {birzai_text}")

load_dotenv()  # Loads Secret from .env file
token = os.getenv("SECRET")  # Replace with your actual token
endpoint = "https://models.github.ai/inference"
model = "openai/gpt-4.1-nano"
client = OpenAI(
    base_url=endpoint,
    api_key=token,
)
print("\nSveiki atvykę į OpenAI asistentą \nUžduokite klausimą apie Biržus arba įveskite 'exit' norėdami išeiti.")
while True:
    question = input("Your question: ")
    if question.lower() == 'exit':
        print("Goodbye!")
        break
    response = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "Tu esi naudingas asistentas suteikti infirmaciją apie Biržų miestelį šiaurės Lietuvoje. Atsakyk visada lietuvių kalba.",
            },
            {
                "role": "user",
                "content": f"{birzai_text} {question}",
            }
        ],
        temperature=1.0,
        top_p=1.0,
        model=model
    )
    print(response.choices[0].message.content)



