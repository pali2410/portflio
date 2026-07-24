import re

with open('assets/Experience-QKEGsRXt.js', 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Update font URLs in Experience JS to use absolute origin resolution
# Replace font:"/fonts/..." with font:(typeof window!=="undefined"?window.location.origin:"")+"/fonts/..."

def replace_font(match):
    font_path = match.group(1)
    return f'font:(typeof window!=="undefined"?window.location.origin:"")+"{font_path}"'

code_updated, count = re.subn(r'font\s*:\s*["\'](/fonts/[^"\']+)["\']', replace_font, code)
print(f"Replaced {count} font relative paths with absolute origin resolution in Experience JS!")

with open('assets/Experience-QKEGsRXt.js', 'w', encoding='utf-8') as f:
    f.write(code_updated)

print("Experience JS font paths updated successfully!")
