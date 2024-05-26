from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task


# Uncomment the following line to use an example of a custom tool
# from polyglot_code_reviewer.tools.custom_tool import MyCustomTool

# Check our tools documentations for more information on how to use them
# from crewai_tools import SerperDevTool

@CrewBase
class PolyglotCodeReviewerCrew():
    """PolyglotCodeReviewer crew"""
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def code_analyzer(self) -> Agent:
        return Agent(
            config=self.agents_config['code_analyzer'],
            # tools=[MyCustomTool()], # Example of custom tool, loaded on the beginning of file
            verbose=True,
            allow_delegation=False
        )

    @agent
    def recommendation_provider(self) -> Agent:
        return Agent(
            config=self.agents_config['recommendation_provider'],
            verbose=True,
            allow_delegation=False
        )

    @agent
    def code_improver(self) -> Agent:
        return Agent(
            config=self.agents_config['code_improver'],
            verbose=True,
            allow_delegation=False
        )

    @agent
    def documentation_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config['documentation_specialist'],
            verbose=True,
            allow_delegation=False
        )

    @task
    def analyze_code(self) -> Task:
        return Task(
            config=self.tasks_config['analyze_code'],
            agent=self.code_analyzer(),
            output_file='.solutions/code_analyzer_report.md'
        )

    @task
    def provide_recommendations(self) -> Task:
        return Task(
            config=self.tasks_config['provide_recommendations'],
            agent=self.recommendation_provider(),
            output_file='.solutions/recommendation_provider_report.md'
        )

    @task
    def improve_code(self) -> Task:
        return Task(
            config=self.tasks_config['improve_code'],
            agent=self.code_improver(),
            output_file='.solutions/code_improver_report.md'
        )

    @task
    def provide_documentation(self) -> Task:
        return Task(
            config=self.tasks_config['document_improvements'],
            agent=self.documentation_specialist(),
            output_file='.solutions/documentation_specialist_report.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the PolyglotCodeReviewer crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=2,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
