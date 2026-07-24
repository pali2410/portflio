import re

with open('assets/Experience-QKEGsRXt.js', 'r', encoding='utf-8') as f:
    code = f.read()

# Fix mobile room camera parameters in Studio & Gallery rooms
old_params = 'zoomDistance:te?2:le?3:ll,panRight:te?0:le?.5:Math.max(.3,n.width/1920*ul),panDown:te?9.7:0,yOffset:te?2.5:le?-3:cl'
new_params = 'zoomDistance:te?3.2:le?3:ll,panRight:te?0:le?.5:Math.max(.3,n.width/1920*ul),panDown:0,yOffset:0'

if old_params in code:
    code = code.replace(old_params, new_params)
    print("Mobile camera panDown and yOffset fixed successfully!")
else:
    print("Warning: old_params exact match failed, using regex replace...")
    code = re.sub(
        r'zoomDistance:te\?2:le\?3:ll,panRight:te\?0:le\?\.5:Math\.max\(\.3,n\.width/1920\*ul\),panDown:te\?9\.7:0,yOffset:te\?2\.5:le\?-3:cl',
        new_params,
        code
    )

with open('assets/Experience-QKEGsRXt.js', 'w', encoding='utf-8') as f:
    f.write(code)

print("Experience-QKEGsRXt.js updated for mobile room visibility!")
