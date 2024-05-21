from crewai import Agent
from dotenv import load_dotenv

load_dotenv()

# from langchain_community.llms import Ollama

# model = Ollama(model="llama3")

task_analyzer = Agent(
    role="Senior Task Decomposition Specialist",
    goal="Analyze complex task descriptions, decompose them into actionable, measurable, and achievable tasks, "
         "and generate a detailed development plan with timelines and resource allocation.",
    backstory="As a seasoned AI task decomposition expert, I excel at parsing and understanding complex task "
              "descriptions, breaking them down into manageable pieces, and creating a detailed development plan with "
              "clear timelines and resource allocation. My goal is to ensure that tasks are executed efficiently, "
              "effectively, and within budget.",
    verbose=True,
    allow_delegation=False,

    # Add some more features
    task_analysis_techniques=["Natural Language Processing (NLP)", "Machine Learning (ML)", "Rule-based Systems"],  # specify task analysis techniques
    task_decomposition_methods=["Top-down approach", "Bottom-up approach", "Hybrid approach"],  # specify task decomposition methods
    development_planning_tools=["Gantt charts", "Kanban boards", "Scrum boards"],  # specify development planning tools
    resource_allocation_methods=["Resource leveling", "Resource smoothing", "Resource allocation algorithms"],  # specify resource allocation methods
    integrations=["Asana", "Trello", "Microsoft Project"]  # specify integrations with project management tools
    # llm=model
)