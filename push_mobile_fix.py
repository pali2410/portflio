import subprocess

try:
    subprocess.run(["git", "add", "."], check=True)
    subprocess.run(["git", "commit", "-m", "Fix mobile camera pan offset to ensure room contents render on mobile devices"], check=True)
    subprocess.run(["git", "push", "origin", "main"], check=True)
    print("Pushed mobile room visibility fix to GitHub successfully!")
except Exception as e:
    print("Git error:", e)
