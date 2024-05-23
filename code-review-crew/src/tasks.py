from textwrap import dedent
from crewai import Task


class CodeReviewTasks:
    def analyze_code_task(self, agent, code):
        return Task(
            description=dedent(f"""\
                    Analyze the provided code for issues and suggest improvements:\n\n{code}"""),
            agent=agent,
            expected_output=dedent(f"""\
                    Analysis of code issues and suggestions for improvement."""),
            output_file="../../.solutions/reviews/code_analysis.md"

        )

    def provide_recommendations_task(self, agent):
        return Task(
            description=dedent(f"""\
                    Provide detailed recommendations and findings based on the analysis from 'analyze_code_task'."""),
            agent=agent,
            expected_output=dedent(f"""\
                    Recommendations for improvement."""),
            output_file="../../.solutions/reviews/recommendations.md"
        )

    def improve_code_task(self, agent):
        return Task(
            description=dedent(f"""\
                    Improve the code based on the recommendations from 'provide_recommendations_task'."""),
            agent=agent,
            expected_output=dedent(f"""\
                    Improved code with optimized performance, reduced errors, and adherence to coding standards."""),
            output_file="../../.solutions/reviews/improved_code.md"
        )

    def document_improvements_task(self, agent):
        return Task(
            description=dedent(f"""\
                    Generate detailed documentation for the improved code and development process 
                    from 'improve_code_task'. Include the code improvements, libraries needed, 
                    and detailed changes made."""),
            agent=agent,
            expected_output=dedent(f"""\
                    User manuals, API documentation, technical guides, and detailed changes and you must include all 
                    the code generated in the process. from 'improve_code_task'"""),
            output_file="../../.solutions/reviews/review_report.md"
        )
