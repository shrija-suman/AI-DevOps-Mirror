import os
from openai import OpenAI

def explain_code(file_path):
    client = OpenAI()

    with open(file_path, "r", encoding="utf-8") as f:
        code = f.read()

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=f"Explain what this code does in simple terms:\n\n{code}"
    )

    print("\nAI Explanation:")
    print(response.output_text)

def main():
    print("Repository Analysis Report")
    print("---------------------------")

    # choose a file to explain
    file_to_explain = "scripts/analyze_repo.py"

    if os.path.exists(file_to_explain):
        explain_code(file_to_explain)
    else:
        print("File not found for explanation")

if __name__ == "__main__":
    main()