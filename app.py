from pathlib import Path
from crewai import Crew, Process
from tasks import build_tasks


def read_text_file(file_path: str) -> str:
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")
    return path.read_text(encoding="utf-8")


def main():
    print("\n=== Quad AI Resume Reviewer ===\n")

    resume_path = input("Enter path to resume text file: ").strip()
    jd_path = input("Enter path to job description text file: ").strip()

    try:
        resume_text = read_text_file(resume_path)
        job_description = read_text_file(jd_path)
    except Exception as e:
        print(f"\nError reading files: {e}")
        return

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

    print("\nRunning Quad AI crew...\n")
    result = crew.kickoff()

    output_file = Path("analysis_output.txt")
    output_file.write_text(str(result), encoding="utf-8")

    print("\n=== Final Output ===\n")
    print(result)
    print(f"\nSaved output to: {output_file.resolve()}")


if __name__ == "__main__":
    main()