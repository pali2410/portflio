import os
import subprocess

# 1. Update package.json - empty dependencies so no heavy node_modules installed on Cloudflare / Netlify
package_json = """{
  "name": "paramveer-portfolio",
  "version": "1.0.0",
  "description": "Paramveer Sinh Zala - Creative 3D & Full-Stack Developer Portfolio",
  "main": "index.html",
  "type": "module",
  "scripts": {
    "build": "echo 'Static build ready'",
    "start": "npx serve -p 3000",
    "dev": "npx serve -p 3000",
    "preview": "npx serve -p 3000"
  },
  "dependencies": {},
  "devDependencies": {}
}
"""

with open("package.json", "w", encoding="utf-8") as f:
    f.write(package_json)
print("Updated package.json without heavy dependencies!")


# 2. Create wrangler.jsonc with assets.exclude rule to exclude node_modules and logs
wrangler_jsonc = """{
  "$schema": "node_modules/wrangler/config-schema.json",
  "name": "portflio",
  "compatibility_date": "2026-07-24",
  "assets": {
    "directory": ".",
    "exclude": [
      "node_modules/**",
      ".git/**",
      ".github/**",
      "*.log",
      ".env",
      "package-lock.json",
      "package.json"
    ]
  }
}
"""

with open("wrangler.jsonc", "w", encoding="utf-8") as f:
    f.write(wrangler_jsonc)
print("Created wrangler.jsonc with node_modules exclusion!")


# 3. Create netlify.toml for seamless Netlify deployment
netlify_toml = """[build]
  publish = "."
  command = "echo 'Static build ready for Netlify'"

[[redirects]]
  from = "/*"
  to = "/index.html"
  status = 200
"""

with open("netlify.toml", "w", encoding="utf-8") as f:
    f.write(netlify_toml)
print("Created netlify.toml for Netlify static deployment!")


# 4. Create _headers file for Cloudflare Pages & Netlify caching
headers_content = """/*
  X-Frame-Options: SAMEORIGIN
  X-Content-Type-Options: nosniff
  Referrer-Policy: strict-origin-when-cross-origin

/textures/*
  Cache-Control: public, max-age=31536000, immutable

/sounds/*
  Cache-Control: public, max-age=31536000, immutable

/assets/*
  Cache-Control: public, max-age=31536000, immutable
"""

with open("_headers", "w", encoding="utf-8") as f:
    f.write(headers_content)
print("Created _headers file for caching & security headers!")

# 5. Git add, commit, push
try:
    subprocess.run(["git", "add", "."], check=True)
    subprocess.run(["git", "commit", "-m", "Fix Cloudflare Wrangler & Netlify asset exclusions"], check=True)
    subprocess.run(["git", "push", "origin", "main"], check=True)
    print("Pushed deployment configuration fixes to GitHub successfully!")
except Exception as e:
    print("Git operation output:", e)
