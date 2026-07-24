import re

with open('assets/Experience-QKEGsRXt.js', 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Fix Ml component text slide offsets so PARAMVEER SINH ZALA and (PALI) stay centered behind character
# Replace 'const S=15;' with 'const S=0;' so text does not fly 12 meters off screen on mobile!
if 'const S=15;' in code:
    code = code.replace('const S=15;', 'const S=0;')
    print("Fixed Ml component text animation offset (S=0) so name stays centered on mobile!")
else:
    print("Warning: const S=15 not found, searching with regex...")
    code = re.sub(r'const S=15\s*;', 'const S=0;', code)

# 2. Add top-level font constants at beginning of file
font_headers = """
const _APP_ORIGIN = (typeof window !== "undefined" && window.location && window.location.origin) ? window.location.origin : "";
const FONT_CABIN_BOLD = _APP_ORIGIN + "/fonts/CabinSketch-Bold.ttf";
const FONT_CABIN_REG = _APP_ORIGIN + "/fonts/CabinSketch-Regular.ttf";
const FONT_RUBIK_SCRIBBLE = _APP_ORIGIN + "/fonts/RubikScribble-Regular.ttf";
"""

code = font_headers + code

# 3. Replace all inline font expressions with top-level static font constants
code = code.replace('(typeof window!=="undefined"?window.location.origin:"")+"/fonts/CabinSketch-Bold.ttf"', 'FONT_CABIN_BOLD')
code = code.replace('(typeof window!=="undefined"?window.location.origin:"")+"/fonts/CabinSketch-Regular.ttf"', 'FONT_CABIN_REG')
code = code.replace('(typeof window!=="undefined"?window.location.origin:"")+"/fonts/RubikScribble-Regular.ttf"', 'FONT_RUBIK_SCRIBBLE')

code = code.replace('"/fonts/CabinSketch-Bold.ttf"', 'FONT_CABIN_BOLD')
code = code.replace('"/fonts/CabinSketch-Regular.ttf"', 'FONT_CABIN_REG')
code = code.replace('"/fonts/RubikScribble-Regular.ttf"', 'FONT_RUBIK_SCRIBBLE')

with open('assets/Experience-QKEGsRXt.js', 'w', encoding='utf-8') as f:
    f.write(code)

print("Experience JS font URLs and character name offset updated successfully!")
