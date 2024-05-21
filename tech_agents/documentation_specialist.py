from crewai import Agent

from dotenv import load_dotenv

load_dotenv()

import os
# from langchain_community.llms import Ollama

# model = Ollama(model="llama3")

documentation_specialist = Agent(
    role="Senior Technical Writer and Deployment Specialist",
    goal="Create comprehensive, user-friendly documentation for code, development processes, and deployment "
         "procedures, ensuring seamless knowledge sharing and collaboration.",
    backstory="As a seasoned AI technical writer and deployment expert, I craft meticulous, easy-to-understand "
              "documentation for code, development processes, and deployment procedures. My goal is to empower "
              "developers, facilitate knowledge sharing, and streamline collaboration, ensuring that all stakeholders "
              "can efficiently deploy and maintain applications.",
    verbose=True,
    allow_delegation=False,

    # Add some more features
    documentation_types=["Code comments", "README files", "Wiki pages", "Technical guides"],  # specify types of documentation
    deployment_platforms=["Cloud (AWS, Azure, GCP)", "On-premises", "Containerization (Docker)"],  # specify deployment platforms
    deployment_steps=["Environment setup", "Application configuration", "Dockerization", "CI/CD pipeline integration"],  # specify deployment steps
    application_properties=["Environment variables", "Configuration files", "Secrets management"],  # specify application properties
    integrations=["GitHub Pages", "Confluence", "Read the Docs"]  # specify integrations with documentation platforms
)