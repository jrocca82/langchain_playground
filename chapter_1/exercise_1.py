from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("LLM_OPEN_AI_KEY")

LLM_OPEN_AI_KEY=api_key
llm = OpenAI(api_key=LLM_OPEN_AI_KEY)

prompt_template = PromptTemplate(
    input_variables=['user_input'],
    template='Generate a creative product idea based on the following industry input: {user_input}'
)

chain = prompt_template | llm

user_input = 'eco-friendly home appliances'

response = chain.invoke(user_input)

print("Creative Product Idea:", response)