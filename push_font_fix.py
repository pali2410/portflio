import subprocess

try:
    subprocess.run(["git", "add", "."], check=True)
    subprocess.run(["git", "commit", "-m", "Fix Troika 3D font URL origin resolution for mobile Safari and Cloudflare Workers"], check=True)
    subprocess.run(["git", "push", "origin", "main"], check=True)
    print("Pushed 3D font URL resolution fix to GitHub successfully!")
except Exception as e:
    print("Git error:", e)
