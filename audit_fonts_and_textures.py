import re

with open('assets/Experience-QKEGsRXt.js', 'r', encoding='utf-8') as f:
    code = f.read()

font_matches = list(re.finditer(r'font\s*:\s*["\'](/fonts/[^"\']+)["\']', code))
print(f"Total font props in Experience JS: {len(font_matches)}")

unique_fonts = set(m.group(1) for m in font_matches)
for uf in sorted(unique_fonts):
    print("  Font file:", uf)
