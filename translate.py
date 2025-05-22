# Write a console application which would translate English text to Lithuanian:
#     - it should read from a input.txt file where English text lays.
#     - if text is more than 200 tokens, then say, the text is too long 
#     and exit the applcication.
#     (Research how calculate tokens)
#     - Write Lithuanian translated text into file lithuanian.txt

import os
from openai import OpenAI
from dotenv import load_dotenv
import tiktoken


load_dotenv()  # Loads Secret from .env file
token = os.getenv("SECRET") # Replace with your actual token
endpoint = "https://models.github.ai/inference"
model = "openai/gpt-4.1-nano"
client = OpenAI(
    base_url=endpoint,
    api_key=token,
)
def count_tokens(text):
    enc = tiktoken.get_encoding("cl100k_base")
    tokens = enc.encode(text)
    return len(tokens)
def translate_text(input_file, output_file):
    """Translates English text to Lithuanian."""
    with open(input_file, 'r', encoding='utf-8') as f:
        english_text = f.read()
    print(f"Original English text: {english_text}")
    token_count = count_tokens(english_text)
    print(f"Token count: {token_count}")
    if token_count > 200:
        print("The text is too long. Please provide a shorter text.")
        return
    response = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant that translates English text to Lithuanian.",
            },
            {
                "role": "user",
                "content": english_text,
            }
        ],
        temperature=1.0,
        top_p=1.0,
        model=model
    )
    translated_text = response.choices[0].message.content
    print(f"Translated Lithuanian text: {translated_text}")
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(translated_text)
if __name__ == "__main__":
    input_file = 'input.txt'
    output_file = 'lithuanian.txt'
    translate_text(input_file, output_file)
    


