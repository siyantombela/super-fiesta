from crewai import Agent
from dotenv import load_dotenv

load_dotenv()

# from langchain_community.llms import Ollama

# model = Ollama(model="llama3")

requirement_specifier = Agent(
    role="Requirement Specifier",
    goal="Convert detailed tasks into clear and concise requirements and specifications.",
    backstory="You are an AI assistant who ensures that task descriptions are translated "
              "into precise and testable technical specifications.",
    verbose=True,
    allow_delegation=False
    # llm=model
)
