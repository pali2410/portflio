import subprocess

try:
    subprocess.run(["git", "add", "."], check=True)
    subprocess.run(["git", "commit", "-m", "Permanently fix mobile room rendering by setting uPaintProgress default to 1 and disabling shader discard rules"], check=True)
    subprocess.run(["git", "push", "origin", "main"], check=True)
    print("Pushed mobile room visibility fix to GitHub successfully!")
except Exception as e:
    print("Git operation output:", e)
