# Quad AI Resume Reviewer

A beginner-friendly Quad AI project using 4 collaborating agents built with CrewAI and Streamlit.

## Features

- 4-agent workflow
  - Planner Agent
  - Resume Analyzer Agent
  - Resume Improver Agent
  - Final Reviewer Agent
- Streamlit web UI
- Terminal version also available
- Downloadable analysis output

## Tech Stack

- Python
- CrewAI
- OpenAI API
- Streamlit
- python-dotenv

## Project Structure

```text
quad-ai-resume-reviewer/
├── app.py
├── agents.py
├── tasks.py
├── streamlit_app.py
├── requirements.txt
├── .env.example
├── .gitignore
├── README.md
└── sample_data/
    ├── sample_resume.txt
    └── sample_job_description.txt