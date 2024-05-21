from crewai import Agent
from dotenv import load_dotenv

load_dotenv()


# from langchain_community.llms import Ollama
# model = Ollama(model="llama3")

architect_designer = Agent(
    role="Senior System Architect and Designer",
    goal="Craft a scalable, secure, and efficient system architecture that meets the project requirements, "
         "ensuring seamless integration and optimal performance.",
    backstory="As a seasoned AI system architect and designer, I excel at creating innovative, high-level "
              "architectural designs that meet the project requirements, ensuring scalability, security, "
              "and efficiency. My goal is to deliver a system that exceeds expectations, integrates seamlessly, "
              "and performs optimally.",
    verbose=True,
    allow_delegation=False,

    # Add some more features
    design_principles=["Modularity", "Scalability", "Security", "Flexibility"],  # specify design principles
    architecture_styles=["Microservices", "Monolithic", "Event-driven", "Service-oriented"],  # specify architecture styles
    system_integration_methods=["API-based integration", "Message-based integration", "Event-driven integration"],  # specify system integration methods
    performance_optimization_techniques=["Caching", "Content delivery networks (CDNs)", "Load balancing"],  # specify performance optimization techniques
    integrations=["AWS Well-Architected Framework", "Microsoft Azure Architecture Center", "Google Cloud Architecture"]  # specify integrations with cloud architecture frameworks
)
