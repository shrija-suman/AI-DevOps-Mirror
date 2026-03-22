import os
import subprocess
from openai import OpenAI

client = OpenAI()

def get_changed_files():
    try:
        result = subprocess.run(
            ["git", "diff", "--name-only", "HEAD~1", "HEAD"],
            capture_output=True,
            text=True
        )
        files = result.stdout.strip().split("\n")
        return [f for f in files if f.endswith((".py", ".js", ".ts", ".java", ".cpp"))]
    except:
        return []

def read_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    except:
        return ""

def analyze_with_ai(code):
    prompt = f"""
You are a senior software engineer.

Analyze the following code and return:

1. Short summary
2. Issues / bugs / bad practices
3. Suggested improvements

Code:
{code}
"""

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )

    return response.output_text

def generate_readme(results):
    content = "# 🪞 AI DevOps Mirror Report\n\n"

    for file, analysis in results.items():
        content += f"## 📄 {file}\n\n"
        content += analysis + "\n\n---\n\n"

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(content)

def main():
    changed_files = get_changed_files()

    if not changed_files or changed_files == ['']:
        print("No changed files detected.")
        return

    results = {}

    for file in changed_files:
        code = read_file(file)
        if code:
            print(f"Analyzing {file}...")
            analysis = analyze_with_ai(code)
            results[file] = analysis

    if results:
        generate_readme(results)
        print("README generated successfully!")

if __name__ == "__main__":
    main()