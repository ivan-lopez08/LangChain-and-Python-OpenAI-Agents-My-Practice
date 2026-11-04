from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

number_of_days = 6
number_of_childs = 3
activity = "music"

prompt_template = PromptTemplate(
    template="""
    Create a travel plan for {days} days,
    for a family with {childs} children,
    who like {activity}
"""
)

prompt = prompt_template.format(
    days = number_of_days,
    childs = number_of_childs,
    activity = activity
)

model = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.5,
    api_key=api_key
)

print(f"Prompt: \n", prompt)

response = model.invoke([
    ("system", "You are a professional trip advisor"),
    ("user", prompt)
    ])

print(response.content)