
import re

with open('assets/Experience-QKEGsRXt.js', 'r', encoding='utf-8') as f:
    content = f.read()

pos = 311955
print('=== COMPONENT USING j / kt() ===')
print(content[max(0, pos-200):min(len(content), pos+1500)])
