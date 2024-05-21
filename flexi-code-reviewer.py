import io
import datetime

from crewai import Task, Crew, Process

from tech_agents.code_generator import code_generator
from tech_agents.code_reviewer import code_reviewer
from tech_agents.documentation_specialist import documentation_specialist
from tech_agents.task_analyzer import task_analyzer

# Read task description from file
with io.open('code-review-task.txt', 'r', encoding='utf-8') as task_description_file:
    task_description = task_description_file.read()

# Define the tasks
understand_code = Task(
    description=f"Analyze the provided code, identify its components, and create a comprehensive code review plan "
                f"to ensure it meets the required standards:\n\n{task_description}",
    agent=task_analyzer,
    expected_output="Detailed code analysis, component breakdown, and a review plan with actionable items."
)

review_code = Task(
    description="Perform a thorough code review of the analyzed code in 'understand_code', identify errors, "
                "optimize performance, and ensure adherence to coding standards and best practices.",
    agent=code_reviewer,
    expected_output="Comprehensive feedback, optimization suggestions, and quality assurance report."
)

generate_improvement_code = Task(
    description="Generate improved code based on the feedback and suggestions from the code review in 'review_code'.",
    agent=code_generator,
    expected_output="Improved code with optimized performance, reduced errors, and adherence to coding standards."
)

# Define the final documentation task
document_all_steps = Task(
    description="Generate a comprehensive final report including all the steps performed, code analysis, review, "
                "and improvement, along with the improved code.",
    agent=documentation_specialist,
    expected_output="Final report including code analysis, review, improvement, and the improved code."
)

# Assemble the Crew
crew = Crew(
    agents=[task_analyzer, code_reviewer, code_generator, documentation_specialist],
    tasks=[understand_code, review_code, generate_improvement_code, document_all_steps],
    verbose=2,
    process=Process.sequential
)


# Kickoff the CrewAI process
output = crew.kickoff()

# Write the output to a Markdown file with a timestamp
timestamp = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
output_filename = f"solutions/reviews/review-{timestamp}.md"
with io.open(output_filename, 'w', encoding='utf-8') as output_file:
    if isinstance(output, dict):
        for task_name, task_output in output.items():
            output_file.write(f"## {task_name}\n\n")
            output_file.write(f"{task_output}\n\n")

        # Specifically include code, libraries, architecture, and tests
        output_file.write("## Implementation Code\n\n")
        output_file.write(output.get('generate_code', 'Code not available') + "\n\n")

        output_file.write("## Required Libraries\n\n")
        output_file.write(output.get('specify_requirements', 'Libraries not specified') + "\n\n")

        output_file.write("## System Architecture\n\n")
        output_file.write(output.get('design_architecture', 'Architecture not specified') + "\n\n")

        output_file.write("## Unit Tests\n\n")
        output_file.write(output.get('generate_unit_tests', 'Unit tests not available') + "\n\n")
    else:
        output_file.write(output)  # Write the output as string if not a dictionary

# Print confirmation
print(f"Output written to '{output_filename}'")