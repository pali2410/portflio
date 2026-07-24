import re

with open('assets/index-DV-1WFZA.js', 'r', encoding='utf-8') as f:
    code = f.read()

font_matches = list(re.finditer(r'font\s*:\s*["\'](/fonts/[^"\']+)["\']', code))
print(f"Total font props in Index JS: {len(font_matches)}")

if font_matches:
    code_updated, count = re.subn(r'font\s*:\s*["\'](/fonts/[^"\']+)["\']', lambda m: f'font:(typeof window!=="undefined"?window.location.origin:"")+"{m.group(1)}"', code)
    with open('assets/index-DV-1WFZA.js', 'w', encoding='utf-8') as f:
        f.write(code_updated)
    print(f"Replaced {count} font relative paths in Index JS!")
else:
    print("No relative font paths in Index JS.")
