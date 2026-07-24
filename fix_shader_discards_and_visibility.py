import re

with open('assets/Experience-QKEGsRXt.js', 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Set default uPaintProgress value to 1 in Fn hook
code = code.replace('uPaintProgress:{value:0}', 'uPaintProgress:{value:1}')

# 2. In shader replace blocks, comment out 'discard;' for room reveal boundary so meshes are ALWAYS 100% visible by default
# Replace 'if (boundary < 0.0) {\n                discard;\n            }' with '// if (boundary < 0.0) discard;'
code = re.sub(
    r'if\s*\(\s*boundary\s*<\s*0\.0\s*\)\s*\{\s*discard\s*;\s*\}',
    '// if (boundary < 0.0) discard;',
    code
)

code = re.sub(
    r'if\s*\(\s*pBoundary\s*<\s*0\.0\s*\)\s*\{\s*discard\s*;\s*\}',
    '// if (pBoundary < 0.0) discard;',
    code
)

code = re.sub(
    r'if\s*\(\s*maskValue\s*<\s*threshold\s*\)\s*discard\s*;',
    '// if (maskValue < threshold) discard;',
    code
)

with open('assets/Experience-QKEGsRXt.js', 'w', encoding='utf-8') as f:
    f.write(code)

print("All shader discard rules modified so 3D room contents remain 100% visible across all mobile devices!")
