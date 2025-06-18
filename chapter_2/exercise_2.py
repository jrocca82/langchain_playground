from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

LLM_OPEN_AI_KEY=api_key
llm = OpenAI(api_key=LLM_OPEN_AI_KEY, temperature=0.3)

prompt_template = PromptTemplate(
    input_variables=['user_input'],
    template='You are a helpful chatbot. User: {user_input}'
)

chain = prompt_template | llm

user_input = input("Enter a story prompt: \n")

response = chain.invoke(user_input)

print("Once upon a time...\n", response)