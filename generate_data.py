import os
import json
import re

base_dir = r"y:\Compilação\Catálogo da umbanda"
html_path = os.path.join(base_dir, 'index.html')

with open(html_path, 'r', encoding='utf-8') as f:
    html_content = f.read()

files = re.findall(r'file:\s*"(.*?)"', html_content)

data_js = "const documentContents = {\n"
for file in files:
    full_path = os.path.join(base_dir, file.replace('/', os.sep))
    if os.path.exists(full_path):
        with open(full_path, 'r', encoding='utf-8') as f:
            content = f.read()
        data_js += f'  {json.dumps(file)}: {json.dumps(content)},\n'
data_js += "};\n"

with open(os.path.join(base_dir, 'data.js'), 'w', encoding='utf-8') as f:
    f.write(data_js)

print("data.js gerado com sucesso!")
