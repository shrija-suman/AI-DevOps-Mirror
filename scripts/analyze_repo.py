from datetime import datetime
import os
from datetime import datetime

def main():
    print("Generating README...")

    files = os.listdir()
    file_count = len(files)

    content = f"""# AI DevOps Mirror Report

Generated on: {datetime.now()}

## Repository Overview
Total Files: {file_count}

## Files in Repository
{chr(10).join(['- ' + f for f in files])}

## Summary
This repository was automatically analyzed by AI DevOps Mirror.

## Insight
Changes in files will automatically reflect in this report.
"""

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(content)

    print("README generated successfully!")

if __name__ == "__main__":
    main()
    
    # demo change