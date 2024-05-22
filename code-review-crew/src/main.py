import io
from datetime import datetime

from dotenv import load_dotenv
from crewai import Crew, Process
from tasks import CodeReviewTasks
from agents import CodeReviewAgents


def main():
    load_dotenv()

    print(f"Welcome to Code Review Crew!")
    print(f"This crew will review your code for issues, optimize code, and recommend improvements.")
    print(f"The crew will be composed of the following agents:\n")
    print(f"  - Code Analyzer")
    print(f"  - Recommendation Provider")
    print(f"  - Code Improver")

    # Read task description from file
    with io.open('../../code-review-task.txt', 'r', encoding='utf-8') as code_review_task_file:
        code_to_review = code_review_task_file.read()
        print(f"Code to review:\n\n{code_to_review}\n\n")
    tasks = CodeReviewTasks()
    agents = CodeReviewAgents()

    code_analyzer_agent = agents.code_analyzer_agent()
    recommendation_provider_agent = agents.recommendation_provider_agent()
    code_improver_agent = agents.code_improver_agent()
    documentation_specialist_agent = agents.documentation_specialist_agent()

    # create tasks
    analyze_code_task = tasks.analyze_code_task(agent=code_analyzer_agent, code=code_to_review)
    provide_recommendations_task = tasks.provide_recommendations_task(agent=recommendation_provider_agent)
    improve_code_task = tasks.improve_code_task(agent=code_improver_agent)
    document_improvements_task = tasks.document_improvements_task(agent=documentation_specialist_agent)

    # add context to tasks
    provide_recommendations_task.context = [analyze_code_task]
    improve_code_task.context = [provide_recommendations_task]
    document_improvements_task.context = [improve_code_task]

    # create crew
    crew = Crew(
        agents=[code_analyzer_agent, recommendation_provider_agent, code_improver_agent, documentation_specialist_agent],
        tasks=[analyze_code_task, provide_recommendations_task, improve_code_task, document_improvements_task],
        verbose=2
    )

    # Kickoff the CrewAI process
    output = crew.kickoff()

    # Write the output to a Markdown file with a timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    with open(f"../../.solutions/flexi-code-reviewer-{timestamp}.md", "w") as f:
        f.write(output)

    print(f"Your code review has been completed and saved to 'flexi-code-reviewer-{timestamp}.md'.")


if __name__ == "__main__":
    main()
