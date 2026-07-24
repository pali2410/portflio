import re

with open('assets/Experience-QKEGsRXt.js', 'r', encoding='utf-8') as f:
    code_exp = f.read()

with open('assets/index-DV-1WFZA.js', 'r', encoding='utf-8') as f:
    code_idx = f.read()

# 1. Check all useTexture / texture loader references
tex_refs_exp = set(re.findall(r'["\'](/textures/[^"\']+)["\']', code_exp))
tex_refs_idx = set(re.findall(r'["\'](/textures/[^"\']+)["\']', code_idx))

all_tex = tex_refs_exp.union(tex_refs_idx)
print(f"Total unique texture path strings found in JS: {len(all_tex)}")

# Replace all texture strings in JS that start with /textures/ to dynamically prefix origin if window is defined
def replace_tex_str(match):
    tex_path = match.group(1)
    return f'(typeof window!=="undefined"?window.location.origin:"")+"{tex_path}"'

# We replace standalone '/textures/...' in useTexture calls or array mappings
# Patterns like "/textures/..." or '/textures/...'
code_exp_fixed, count_exp = re.subn(r'["\'](/textures/[^"\']+)["\']', replace_tex_str, code_exp)
print(f"Replaced {count_exp} texture paths in Experience JS with absolute origin resolution!")

code_idx_fixed, count_idx = re.subn(r'["\'](/textures/[^"\']+)["\']', replace_tex_str, code_idx)
print(f"Replaced {count_idx} texture paths in Index JS with absolute origin resolution!")

with open('assets/Experience-QKEGsRXt.js', 'w', encoding='utf-8') as f:
    f.write(code_exp_fixed)

with open('assets/index-DV-1WFZA.js', 'w', encoding='utf-8') as f:
    f.write(code_idx_fixed)

print("All texture paths in JS bundles now resolve absolute origin dynamically!")
