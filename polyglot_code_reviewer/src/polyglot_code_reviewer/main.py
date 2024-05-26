#!/usr/bin/env python
import io
import os

import agentops
from dotenv import load_dotenv

from src.polyglot_code_reviewer.crew import PolyglotCodeReviewerCrew


def run():
    load_dotenv()
    agentops.init(os.getenv('AGENT_OPS_API_KEY'))

    with io.open('code-review-task.txt', 'r', encoding='utf-8') as code_review_task_file:
        code_to_review = code_review_task_file.read()

    inputs = {
        'code': code_to_review
    }

    PolyglotCodeReviewerCrew().crew().kickoff(inputs=inputs)
