from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from pydantic import Field, BaseModel
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

class City(BaseModel):
    city: str = Field(description="A city recommended to visit")
    reason: str = Field(description="The reason why would be interesting to visit this city")

class Restaurants(BaseModel):
    city:str = Field(description="The city recommended to visit")
    restaurants:str = Field(description="Recommended restaurants on that city")


parser_city = JsonOutputParser(pydantic_object=City)
parser_restaurant = JsonOutputParser(pydantic_object=Restaurants)
    

prompt_city = PromptTemplate(
    template="""
    Suggest a city to visit based on my interest on {interest}.
    {output_format}
    """,
    input_variables=["interest"],
    partial_variables={"output_format": parser_city.get_format_instructions()}
)

prompt_restaurant = PromptTemplate(
    template="""
    Suggest popular restaurants from the locals on the city {city}.
    {output_format}
    """,
    partial_variables={"output_format": parser_restaurant.get_format_instructions()}
)

prompt_culture = PromptTemplate(
    template="Suggest activities and places to see on {city}."
)

model = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.5,
    api_key=api_key
)

chain_1 = prompt_city | model | parser_city
chain_2 = prompt_restaurant | model | parser_restaurant
chain_3 = prompt_culture | model | StrOutputParser()

chain_main = (chain_1 | chain_2 | chain_3)

response = chain_main.invoke({"interest": "beach"})

print(response)