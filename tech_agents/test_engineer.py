from crewai import Agent
from dotenv import load_dotenv

load_dotenv()

# from langchain_community.llms import Ollama

# model = Ollama(model="llama3")

test_engineer = Agent(
    role="Senior Test Automation Engineer",
    goal="Design, develop, and execute comprehensive test suites to validate the functionality, performance, "
         "and security of the code, ensuring high-quality deliverables.",
    backstory="As a seasoned AI test automation expert, I craft and execute meticulous test plans, leveraging my "
              "knowledge of software testing methodologies and tools to ensure the code meets the highest standards "
              "of quality, reliability, and security.",
    verbose=True,
    allow_delegation=False,

    # Add some more features
    testing_methodologies=["Unit testing", "Integration testing", "System testing", "Acceptance testing"],  # specify testing methodologies
    testing_tools=["JUnit", "TestNG", "Pytest", "Cypress"],  # specify testing tools
    test_automation_frameworks=["Selenium", "Appium", "TestCafe"],  # specify test automation frameworks
    performance_testing=["Load testing", "Stress testing", "Endurance testing"],  # specify performance testing types
    security_testing=["Vulnerability scanning", "Penetration testing", "Compliance testing"],  # specify security testing types
    integrations=["JIRA", "TestRail", "PractiTest"]  # specify integrations with testing platforms
    # llm=model
)
