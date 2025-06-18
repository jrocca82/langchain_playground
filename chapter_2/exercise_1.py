# This file requires openai 0.28.0
import openai
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

openai.api_key = api_key

def get_chat_completion(user_prompt):
    response = openai.ChatCompletion.create(
        model = 'gpt-3.5-turbo',
        messages=[{"role": "user", "content": user_prompt}]
    )
    return response.choices[0].message.content.strip()

user_prompt = input("Enter a story prompt: \n")

result = get_chat_completion(user_prompt)

print(result)