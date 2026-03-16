import os
from openai import OpenAI

def explain_code(file_path):
    try:
        client = OpenAI()

        with open(file_path, "r", encoding="utf-8") as f:
            code = f.read()

        response = client.responses.create(
            model="gpt-4.1-mini",
            input=f"Explain what this code does in simple terms:\n\n{code}"
        )

        print("\nAI Explanation:")
        print(response.output_text)

    except Exception as e:
        print("\nAI service unavailable.")
        print("Fallback explanation:")
        print("This script scans repository files and counts lines of code to generate a basic analysis report.")

def main():
    print("Repository Analysis Report")
    print("---------------------------")

    file_to_explain = "scripts/analyze_repo.py"

    if os.path.exists(file_to_explain):
        explain_code(file_to_explain)
    else:
        print("File not found.")

if __name__ == "__main__":
    main()