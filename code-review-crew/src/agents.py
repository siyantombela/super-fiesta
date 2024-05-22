from textwrap import dedent
from crewai import Agent


class CodeReviewAgents:
    def code_analyzer_agent(self):
        return Agent(
            role="Code Analyzer",
            goal=dedent("""\
                    Analyze provided code for issues, make recommendations, and suggest improvements."""),

            backstory=dedent("""\
                    You are an AI assistant specializing in code analysis to identify issues, optimize code, 
                    and recommend improvements."""),
            verbose=True,
            allow_delegation=False,
            expertise=["code analysis", "software development", "security analysis"],
            personality=["meticulous", "analytical", "communicative", "organized", "problem solver"],
        )

    def recommendation_provider_agent(self):
        return Agent(
            role="Recommendation Provider",
            goal=dedent("""\
                    Provide detailed recommendations and findings based on the code analysis from 'code_analyzer_agent'."""),

            backstory=dedent("""\
                    You are an AI assistant specializing in providing detailed recommendations and findings based 
                    on the analysis from 'code_analyzer_agent'."""),
            verbose=True,
            allow_delegation=False,
            expertise=["technical writing", "software development", "requirements analysis"],
            personality=["meticulous", "analytical", "communicative", "organized", "problem solver"],
        )

    def code_improver_agent(self):
        return Agent(
            role="Code Improver",
            goal=dedent("""\
                    Improve the code based on the recommendations from 'recommendation_provider_agent'."""),

            backstory=dedent("""\
                    You are an AI assistant specializing in improving the code based on the recommendations from 
                    'recommendation_provider_agent'."""),
            verbose=True,
            allow_delegation=False,
            language_support=["Java", "Python", "C++", "JavaScript", "TypeScript"],
            architecture=["Web Application", "Mobile App", "Desktop App", "Microservices", "Cloud Native"],
            design_patterns=["MVC", "MVVM", "Repository Pattern", "Factory Pattern", "Observer Pattern"],
            coding_standards=["SOLID principles", "Clean Code", "Test-Driven Development"],
            integrations=["API Integration", "Database Integration", "Third-Party Library Integration"],
            context=["recommendation_provider_agent"]
        )

    def documentation_specialist_agent(self):
        return Agent(
            role="Senior Technical Writer and Deployment Specialist",
            goal=dedent("""\
                    Generate comprehensive documentation for the improved code and the development process."""),

            backstory=dedent("""\
                    As a seasoned AI technical writer and deployment expert, I craft meticulous, easy-to-understand 
                    documentation for code, development processes, and deployment procedures. My goal is to empower 
                    developers, facilitate knowledge sharing, and streamline collaboration, ensuring that all stakeholders 
                    can efficiently deploy and maintain applications, leveraging the improved code quality and 
                    architecture resulting from the code review task."""),
            verbose=True,
            allow_delegation=False,
            documentation_types=["Code comments", "README files", "Wiki pages", "Technical guides"],
            deployment_platforms=["Cloud (AWS, Azure, GCP)", "On-premises", "Containerization (Docker)"],
            deployment_steps=["Environment setup", "Application configuration", "Dockerization",
                              "CI/CD pipeline integration"],
            application_properties=["Environment variables", "Configuration files", "Secrets management"],
            integrations=["GitHub Pages", "Confluence", "Read the Docs"],
            refactored_code_consideration=True,
            code_included_in_report=True,
            context=["code_improver_agent"]
        )
