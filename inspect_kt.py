
import re

with open('assets/Experience-QKEGsRXt.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Find kt definition
kt_defs = list(re.finditer(r'(?:const|let|var|function|,)\s*kt\s*=\s*|\bfunction kt\(', content))
print(f'kt definitions: {len(kt_defs)}')
for m in kt_defs[:3]:
    print(' ', repr(content[max(0, m.start()-20):m.end()+250])[:300])
