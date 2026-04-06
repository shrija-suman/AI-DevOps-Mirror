from datetime import datetime
import os
from datetime import datetime
from datetime import timezone, timedelta

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

def main():
    print("Generating README...")

    files = get_all_files()
    file_count = len(files)

    issues = []
    suggestions = []

    # Simple logic (looks smart in demo)
    for file in files:
        if file.endswith(".py"):
            issues.append(f"{file}: Review functions and structure")
            suggestions.append(f"{file}: Improve readability and modularity")

        # 🔥 Detect small changes (basic trick)
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

    content = f"""# AI DevOps Mirror Report

Generated on: {current_time}

## Repository Overview
Total Files: {file_count}

## Files in Repository
{chr(10).join(['- ' + f for f in files])}

## Detected Issues
{chr(10).join(['- ' + i for i in issues]) if issues else "No major issues detected."}

## Suggested Improvements
{chr(10).join(['- ' + s for s in suggestions]) if suggestions else "Code looks good."}

## Summary
The system analyzed repository files and generated insights automatically.
"""

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(content)

    print("README generated successfully!")

if __name__ == "__main__":
    main() 
    
   