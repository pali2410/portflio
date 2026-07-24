with open('assets/Experience-QKEGsRXt.js', 'r', encoding='utf-8') as f:
    code = f.read()

pos = code.find('Ca=')
if pos != -1:
    print("Ca component snippet:")
    print(code[pos:pos+1500].encode('ascii', 'ignore').decode('ascii'))
