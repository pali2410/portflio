import subprocess

try:
    subprocess.run(["git", "add", "."], check=True)
    subprocess.run(["git", "commit", "-m", "Center character name PARAMVEER SINH ZALA (PALI) for mobile viewports and use static top-level font constants"], check=True)
    subprocess.run(["git", "push", "origin", "main"], check=True)
    print("Pushed character name & mobile 3D font fix to GitHub successfully!")
except Exception as e:
    print("Git operation output:", e)
