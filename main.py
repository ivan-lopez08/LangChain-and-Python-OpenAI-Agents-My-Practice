from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

number_of_days = 6
number_of_childs = 3
activity = "Hiking"

prompt = f"Create a travel plan for {number_of_days} days, for a family with {number_of_childs} children, who like {activity}"

client = OpenAI(api_key=api_key)

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role" : "system",
            "content" : "You are a trip advisor."
        },
        {
            "role" : "user",
            "content" : prompt
        }
    ]
)

response_in_text = response.choices[0].message.content
print(response_in_text)