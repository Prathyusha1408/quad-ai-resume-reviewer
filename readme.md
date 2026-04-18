# Quad AI Resume Reviewer

This project is a multi-agent AI system that analyzes and improves resumes using a coordinated workflow of specialized agents.

It demonstrates how multiple AI agents can collaborate to solve a real-world problem: improving resume quality based on job descriptions.

## Features

- Multi-agent workflow using CrewAI
- Resume analysis and feedback generation
- Resume improvement suggestions based on job requirements
- Final review and validation
- Streamlit-based interactive UI
- Terminal-based execution support
- Downloadable output reports
## How It Works (Agent Workflow)

The system uses 4 agents working sequentially:
1. Planner Agent  
   - Understands the task and defines the workflow
2. Resume Analyzer Agent  
   - Extracts key information from the resume  
   - Identifies missing skills and weaknesses  
3. Resume Improver Agent  
   - Suggests improvements based on job description  
   - Enhances content quality  
4. Final Reviewer Agent  
   - Validates output  
   - Ensures clarity and completeness  
Each agent passes its output to the next, forming a pipeline.

## Tech Stack

- Python (core logic)
- CrewAI (multi-agent orchestration)
- OpenAI API (LLM processing)
- Streamlit (UI)
- python-dotenv (environment management)

## Challenges Faced

- Designing agent interaction flow
- Handling unstructured resume text
- Ensuring meaningful AI-generated feedback

## Future Improvements

- Add scoring system for resumes
- Integrate job-role matching
- Store results in a database
- Improve UI/UX

## How to Run

1. Clone the repository
2. Install dependencies:
```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
