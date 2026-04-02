import os
from crewai import Agent, LLM
from dotenv import load_dotenv

load_dotenv()

MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

llm = LLM(
    model=f"openai/{MODEL}",
    temperature=0.2
)

planner_agent = Agent(
    role="Resume Review Planner",
    goal="Understand the job description and create a checklist of what a strong resume should contain for this role.",
    backstory=(
        "You are an expert hiring strategist. "
        "You break job descriptions into clear evaluation criteria like skills, tools, keywords, and experience expectations."
    ),
    llm=llm,
    verbose=True
)

analyzer_agent = Agent(
    role="Resume Analyzer",
    goal="Compare the resume against the checklist and identify strengths, gaps, and missing keywords.",
    backstory=(
        "You are an ATS and recruiter expert. "
        "You carefully compare resumes to job requirements and identify mismatches."
    ),
    llm=llm,
    verbose=True
)

improver_agent = Agent(
    role="Resume Improver",
    goal="Rewrite weak resume bullet points and suggest stronger, ATS-friendly improvements.",
    backstory=(
        "You are a resume writing specialist who transforms plain bullet points into achievement-oriented, measurable statements."
    ),
    llm=llm,
    verbose=True
)

reviewer_agent = Agent(
    role="Final Reviewer",
    goal="Provide a final score, summary, and next steps based on all previous agent outputs.",
    backstory=(
        "You are a senior hiring manager. "
        "You provide practical, clear, final feedback and a realistic overall fit assessment."
    ),
    llm=llm,
    verbose=True
)