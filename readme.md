# Quad AI Resume Reviewer

A beginner-friendly Quad AI project using 4 collaborating agents built with CrewAI.

## What this project does

This project takes:
- a resume
- a job description

Then 4 AI agents work in sequence:

1. Planner Agent
2. Resume Analyzer Agent
3. Resume Improver Agent
4. Final Reviewer Agent

## Tech Stack

- Python
- CrewAI
- OpenAI API
- dotenv

## Project Structure

```text
quad-ai-resume-reviewer/
├── app.py
├── agents.py
├── tasks.py
├── requirements.txt
├── .env.example
├── README.md
└── sample_data/
    ├── sample_resume.txt
    └── sample_job_description.txt