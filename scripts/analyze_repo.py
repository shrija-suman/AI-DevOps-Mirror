from datetime import datetime, timezone, timedelta
import os
import subprocess

# IST Time
ist = timezone(timedelta(hours=5, minutes=30))
current_time = datetime.now(ist)

def get_all_files():
    """Return all files in repo except .git"""
    files = []
    for root, dirs, filenames in os.walk("."):
        if ".git" in root:
            continue
        for f in filenames:
            files.append(os.path.join(root, f))
    return files

def get_git_diff():
    """Return the latest commit diff"""
    try:
        result = subprocess.run(
            ["git", "diff", "HEAD~1", "HEAD"],
            capture_output=True,
            text=True
        )
        diff = result.stdout.strip()
        return diff if diff else "No changes detected."
    except:
        return "Could not fetch git diff."

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

    # 🔥 Include Git diff for green/red highlights
    diff_output = get_git_diff()

    content = f"""# 🪞 AI DevOps Mirror Report

🕒 Generated on: {current_time}

---

## 🔍 Code Changes (Latest Commit)

```diff
{diff_output}
```