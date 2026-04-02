from pathlib import Path
import streamlit as st
from crewai import Crew, Process
from tasks import build_tasks


st.set_page_config(
    page_title="Quad AI Resume Reviewer",
    page_icon="📄",
    layout="wide"
)


def run_quad_ai(resume_text: str, job_description: str) -> str:
    tasks = build_tasks(resume_text, job_description)

    crew = Crew(
        agents=[
            tasks[0].agent,
            tasks[1].agent,
            tasks[2].agent,
            tasks[3].agent,
        ],
        tasks=tasks,
        process=Process.sequential,
        verbose=True
    )

    result = crew.kickoff()
    return str(result)


def load_sample_file(file_path: str) -> str:
    path = Path(file_path)
    if path.exists():
        return path.read_text(encoding="utf-8")
    return ""


st.title("Quad AI Resume Reviewer")
st.markdown("A simple 4-agent AI system to analyze and improve resumes against job descriptions.")

with st.sidebar:
    st.header("Options")
    use_sample = st.checkbox("Load sample data")
    st.markdown("Use sample resume and job description for quick testing.")

if use_sample:
    default_resume = load_sample_file("sample_data/sample_resume.txt")
    default_jd = load_sample_file("sample_data/sample_job_description.txt")
else:
    default_resume = ""
    default_jd = ""

col1, col2 = st.columns(2)

with col1:
    st.subheader("Resume")
    resume_text = st.text_area(
        "Paste resume text here",
        value=default_resume,
        height=350,
        placeholder="Paste the full resume text here..."
    )

with col2:
    st.subheader("Job Description")
    job_description = st.text_area(
        "Paste job description here",
        value=default_jd,
        height=350,
        placeholder="Paste the full job description here..."
    )

run_button = st.button("Run Quad AI Review", use_container_width=True)

if run_button:
    if not resume_text.strip() or not job_description.strip():
        st.error("Please provide both resume text and job description.")
    else:
        with st.spinner("Running 4 AI agents..."):
            try:
                result = run_quad_ai(resume_text, job_description)

                output_file = Path("analysis_output.txt")
                output_file.write_text(result, encoding="utf-8")

                st.success("Review completed successfully.")

                st.subheader("Final Output")
                st.text_area("Result", value=result, height=500)

                st.download_button(
                    label="Download Result",
                    data=result,
                    file_name="analysis_output.txt",
                    mime="text/plain"
                )

            except Exception as e:
                st.error(f"Error: {e}")