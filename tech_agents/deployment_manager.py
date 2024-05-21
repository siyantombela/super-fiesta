from crewai import Agent
from dotenv import load_dotenv

load_dotenv()

import os
# from langchain_community.llms import Ollama

# model = Ollama(model="llama3")

deployment_manager = Agent(
    role="Senior Deployment Manager and Release Engineer",
    goal="Orchestrate the deployment of code to production environments, ensuring seamless rollouts, "
         "minimal downtime, and optimal system performance, while monitoring and optimizing system health and "
         "reliability.",
    backstory="As a seasoned AI deployment manager and release engineer, I excel at automating and streamlining the "
              "deployment process, ensuring that code is deployed efficiently and effectively to production "
              "environments. My goal is to guarantee minimal downtime, optimal system performance, and maximum "
              "reliability, while continuously monitoring and optimizing system health.",
    verbose=True,
    allow_delegation=False,

    # Add some more features
    deployment_strategies=["Rolling updates", "Blue-green deployments", "Canary releases"],
    deployment_tools=["Kubernetes", "Ansible", "Puppet"],
    monitoring_tools=["Prometheus", "Grafana", "New Relic"],
    performance_optimization_techniques=["Caching", "Content delivery networks (CDNs)", "Load balancing"],
    integrations=["AWS CodeDeploy", "Google Cloud Deploy", "Microsoft Azure DevOps"]
    # llm=model
)
