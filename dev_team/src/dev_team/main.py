#!/usr/bin/env python
from dev_team.crew import DevTeamCrew


def run():
    # Replace with your inputs, it will automatically interpolate any tasks and agents information
    inputs = {
        'topic': 'AI LLMs'
    }
    DevTeamCrew().crew().kickoff(inputs=inputs)