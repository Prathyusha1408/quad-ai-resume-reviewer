from crewai import Task
from agents import planner_agent, analyzer_agent, improver_agent, reviewer_agent


def build_tasks(resume_text: str, job_description: str):
    planner_task = Task(
        description=f"""
Analyze the following job description and create a structured checklist.

Job Description:
{job_description}

Your output must include:
1. Required technical skills
2. Preferred technical skills
3. Important ATS keywords
4. Expected experience level
5. Suggested evaluation checklist (5 to 10 points)
""",
        expected_output="A structured hiring checklist with required skills, preferred skills, keywords, and evaluation points.",
        agent=planner_agent
    )

    analyzer_task = Task(
        description=f"""
Use the job-description checklist and compare it against this resume.

Resume:
{resume_text}

You must:
1. Identify strengths in the resume
2. Identify missing skills or keywords
3. Point out weak sections
4. Explain how well the resume matches the target job
""",
        expected_output="A gap analysis showing strengths, weaknesses, missing keywords, and match quality.",
        agent=analyzer_agent
    )

    improver_task = Task(
        description=f"""
Improve the resume based on the prior analysis.

Resume:
{resume_text}

Requirements:
1. Rewrite 3 to 5 bullet points in stronger language
2. Add ATS-friendly wording
3. Keep improvements realistic
4. Do not invent fake experience
""",
        expected_output="Improved resume bullet points and practical suggestions for stronger ATS alignment.",
        agent=improver_agent
    )

    reviewer_task = Task(
        description="""
Review all prior outputs from the planner, analyzer, and improver.

Provide:
1. Final score out of 10
2. One short summary paragraph
3. Top 5 next actions for the candidate
4. Final hiring fit level: Strong Fit / Moderate Fit / Weak Fit
""",
        expected_output="A final score, summary, next-step recommendations, and hiring fit level.",
        agent=reviewer_agent
    )

    return [planner_task, analyzer_task, improver_task, reviewer_task]