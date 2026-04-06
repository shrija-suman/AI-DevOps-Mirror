# AI DevOps Mirror Report

Generated on: 2026-04-06 10:07:58

---

## 📊 Repository Overview
Total Files: 7

---

## 📂 Files in Repository
- requirements.txt
- README.md
- scripts/analyze_repo.py
- scripts/README.md
- docker/Dockerfile
- docker/README.md
- docs/README.md

---

## ⚠️ Detected Issues
- requirements.txt: Non-code file detected
- scripts/analyze_repo.py: Check functions and structure

---

## 💡 Suggested Improvements
- requirements.txt: Organize or document properly
- README.md: Ensure proper usage
- scripts/analyze_repo.py: Improve readability/modularity
- scripts/README.md: Ensure proper usage
- docker/Dockerfile: Ensure proper usage
- docker/README.md: Ensure proper usage
- docs/README.md: Ensure proper usage

---

## 🔍 Code Changes (Git Diff)
diff --git a/scripts/analyze_repo.py b/scripts/analyze_repo.py
index 2260c9d..e175e33 100644
--- a/scripts/analyze_repo.py
+++ b/scripts/analyze_repo.py
@@ -4,7 +4,7 @@ import subprocess
 
 # IST Time
 ist = timezone(timedelta(hours=5, minutes=30))
- current_time = datetime.now(ist).strftime("%Y-%m-%d %H:%M:%S %Z")
+ current_time = datetime.now(ist).strftime("%Y-%m-%d %H:%M:%S")
 
 def get_all_files():
     files = []
@@ -12,7 +12,7 @@ def get_all_files():
         if ".git" in root:
             continue
         for f in filenames:
-             files.append(os.path.join(root, f))
+             files.append(os.path.relpath(os.path.join(root, f)))
     return files
 
 def get_git_diff():
@@ -23,26 +23,22 @@ def get_git_diff():
             text=True
         )
         diff = result.stdout
- 
         if not diff.strip():
             return "No changes detected."
- 
-         # Convert diff to GitHub style: + green, - red
         diff_lines = diff.splitlines()
         formatted_diff = []
         for line in diff_lines:
             if line.startswith("+") and not line.startswith("+++"):
-                 formatted_diff.append(f"<span style='color:green;'>+ {line[1:]}</span>")
+                 formatted_diff.append(f"+ {line[1:]}")
             elif line.startswith("-") and not line.startswith("---"):
-                 formatted_diff.append(f"<span style='color:red;'>- {line[1:]}</span>")
+                 formatted_diff.append(f"- {line[1:]}")
             else:
                 formatted_diff.append(line)
         return "\n".join(formatted_diff)
- 
     except Exception as e:
         return f"Could not fetch git diff: {e}"
 
- def main():
+ def generate_readme():
     print("Generating README...")
 
     files = get_all_files()
@@ -53,27 +49,24 @@ def main():
 
     for file in files:
         if file.endswith(".py"):
-             issues.append(f"{file}: Review functions and structure")
-             suggestions.append(f"{file}: Improve readability and modularity")
+             issues.append(f"{file}: Check functions and structure")
+             suggestions.append(f"{file}: Improve readability/modularity")
             try:
                 with open(file, "r", encoding="utf-8") as f:
                     lines = f.readlines()
                     if len(lines) < 5:
                         issues.append(f"{file}: File too small, may lack logic")
-             except Exception as e:
-                 issues.append(f"{file}: Could not read file ({e})")
- 
+             except:
+                 issues.append(f"{file}: Could not read file")
         elif file.endswith(".txt"):
             issues.append(f"{file}: Non-code file detected")
-             suggestions.append(f"{file}: Consider organizing or documenting properly")
- 
+             suggestions.append(f"{file}: Organize or document properly")
         else:
             suggestions.append(f"{file}: Ensure proper usage")
 
-     # Get Git diff
     diff_output = get_git_diff()
 
-     content = f'''# AI DevOps Mirror Report
+     content = f"""# AI DevOps Mirror Report
 
 Generated on: {current_time}
 
@@ -101,13 +94,22 @@ Total Files: {file_count}
 
 ## 🔍 Code Changes (Git Diff)
 {diff_output}
- '''
+ """
 
-     # Write Markdown README
-     with open("AI_DevOps_Mirror_Report.md", "w", encoding="utf-8") as f:
+     # Overwrite README.md
+     with open("README.md", "w", encoding="utf-8") as f:
         f.write(content)
+     print("README.md updated!")
 
-     print("README generated successfully!")
+ def git_commit_push():
+     try:
+         subprocess.run(["git", "add", "README.md"], check=True)
+         subprocess.run(["git", "commit", "-m", "Auto-update README"], check=True)
+         subprocess.run(["git", "push", "origin", "main"], check=True)
+         print("Changes committed and pushed to GitHub!")
+     except subprocess.CalledProcessError as e:
+         print("Git push failed:", e)
 
 if __name__ == "__main__":
-     main()
\ No newline at end of file
+     generate_readme()
+     git_commit_push()
\ No newline at end of file
