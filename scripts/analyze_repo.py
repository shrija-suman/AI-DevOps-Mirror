from datetime import datetime, timezone, timedelta
import os
import subprocess

# IST Time
ist = timezone(timedelta(hours=5, minutes=30))
current_time = datetime.now(ist)

def get_all_files():
    files = []
    for root, dirs, filenames in os.walk("."):
        if ".git" in root:
            continue
        for f in filenames:
            files.append(os.path.join(root, f))
    return files

def get_git_diff():
    try:
        result = subprocess.run(
            ["git", "diff", "HEAD~1", "HEAD"],
            capture_output=True,
            text=True
        )
        diff = result.stdout

        if not diff.strip():
            return "No changes detected."

        # Convert diff to GitHub style: + green, - red
        diff_lines = diff.splitlines()
        formatted_diff = []
        for line in diff_lines:
            if line.startswith("+") and not line.startswith("+++"):
                formatted_diff.append(f"<span style='color:green;'>+ {line[1:]}</span>")
            elif line.startswith("-") and not line.startswith("---"):
                formatted_diff.append(f"<span style='color:red;'>- {line[1:]}</span>")
            else:
                formatted_diff.append(line)
        return "\n".join(formatted_diff)

    except Exception as e:
        return f"Could not fetch git diff: {e}"

def main():
    print("Generating README...")

    files = get_all_files()
    file_count = len(files)

    issues = []
    suggestions = []

    for file in files:
        if file.endswith(".py"):
            issues.append(f"{file}: Review functions and structure")
            suggestions.append(f"{file}: Improve readability and modularity")
            try:
                with open(file, "r", encoding="utf-8") as f:
                    lines = f.readlines()
                    if len(lines) < 5:
                        issues.append(f"{file}: File too small, may lack logic")
            except:
                issues.append(f"{file}: Could not read file")

        elif file.endswith(".txt"):
            issues.append(f"{file}: Non-code file detected")
            suggestions.append(f"{file}: Consider organizing or documenting properly")

        else:
            suggestions.append(f"{file}: Ensure proper usage")

    # Get Git diff
    diff_output = get_git_diff()

    content = f'''# AI DevOps Mirror Report

Generated on: {current_time}

---

## 📊 Repository Overview
Total Files: {file_count}

---

## 📂 Files in Repository
{chr(10).join(['- ' + f for f in files])}

---

## ⚠️ Detected Issues
{chr(10).join(['- ' + i for i in issues]) if issues else "No major issues detected."}

---

## 💡 Suggested Improvements
{chr(10).join(['- ' + s for s in suggestions]) if suggestions else "Code looks good."}

---

## 🔍 Code Changes (Git Diff)

{diff_output}
'''

    # Write Markdown README
    with open("AI_DevOps_Mirror_Report.md", "w", encoding="utf-8") as f:
        f.write(content)

    print("README generated successfully!")

if __name__ == "__main__":
    main()
    
    import subprocess

subprocess.run(["git", "add", "README.md"])
subprocess.run(["git", "commit", "--allow-empty", "-m", "Auto-update README"])
subprocess.run(["git", "push", "origin", "main"])