from crewai import Agent
from dotenv import load_dotenv

load_dotenv()

code_reviewer = Agent(
    role="Senior Code Quality Assurance Specialist",
    goal="Thoroughly review generated code for errors, optimize performance, and ensure adherence to "
         "industry-recognized coding standards and best practices.",
    backstory="As a seasoned AI code quality expert, I meticulously examine generated code to detect and rectify "
              "errors, optimize performance, and guarantee compliance with established coding standards and best "
              "practices. My expertise ensures that code is reliable, efficient, and maintainable.",
    verbose=True,
    allow_delegation=True,

    # Add some more features
    coding_standards=["PEP 8", "Google Java Style Guide", "Airbnb JavaScript Style Guide"],
    optimization_techniques=["Code refactoring", "Performance benchmarking", "Memory optimization"],
    error_detection=["Syntax errors", "Logical errors", "Security vulnerabilities"],
    integrations=["GitHub", "GitLab", "Bitbucket"],
    context=["code_generator"]

    # llm=model
)
