with open('assets/Experience-QKEGsRXt.js', 'r', encoding='utf-8') as f:
    code = f.read()

pos = code.find('/textures/entrance/sign.webp')
if pos != -1:
    print("Sign texture snippet:")
    print(code[max(0, pos-100):min(len(code), pos+200)].encode('ascii', 'ignore').decode('ascii'))

pos2 = code.find('/fonts/CabinSketch-Bold.ttf')
if pos2 != -1:
    print("\nFont snippet:")
    print(code[max(0, pos2-100):min(len(code), pos2+200)].encode('ascii', 'ignore').decode('ascii'))
