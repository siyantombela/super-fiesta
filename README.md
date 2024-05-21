Flexi Tech Team Documentation
=============================================

 Overview
------------

This documentation provides a comprehensive guide to the Flexi Tech Team application, a cutting-edge technology that streamlines software development by automating various tasks. The application's capabilities include task analysis, requirement specification, architecture design, code generation, code review, unit testing, and documentation.

 Getting Started
---------------

### Prerequisites

* Python 3.x
* CrewAI library
* GROQ API key (for llama3-70b-8192 model)

### Setting Up the Environment

To set up the environment, follow these steps:

1. Clone the repository and navigate to the project directory.
2. Create a file named `development-task.txt` in the project directory, containing the task description.
3. Set the following environment variables:

- **OPENAI_API_BASE**='https://api.groq.com/openai/v1' 
- **OPENAI_MODEL_NAME**='llama3-70b-8192'
- **OPENAI_API_KEY**='YOUR_GROQ_APIKEY'

**Important:** Replace `YOUR_GROQ_APIKEY` with your actual GROQ API key. **Do not hardcode your API key in the code or documentation.**

### Running the Project

1. Run the script using Python: `python flexi-tech-team.py`
2. The output will be written to a Markdown file with a timestamp in the `solutions` directory.


 Contributing
------------

Contributions are welcome! If you'd like to contribute to this project, please fork the repository and submit a pull request.

 Acknowledgments
---------------

This project uses the CrewAI library and the llama3-70b-8192 model. We acknowledge the authors and maintainers of these projects for their contributions to the AI and NLP communities.