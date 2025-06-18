import openai
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

openai.api_key = api_key

# client = openai.Client()

# response = client.completions.create(
#     model='davinci-002', # This model sux lol wut
#     prompt='What is machine learning?',
#     max_tokens=300
# )

# print(response.choices[0].text)

def get_chat_completion(user_prompt):
    response = openai.ChatCompletion.create(
        model = 'gpt-3.5-turbo',
        messages=[{"role": "user", "content": user_prompt}]
    )
    return response.choices[0].message.content.strip()

user_prompt = input("Enter a story prompt: \n")

result = get_chat_completion(user_prompt)

print(result)