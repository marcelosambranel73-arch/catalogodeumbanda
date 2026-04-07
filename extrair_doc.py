import os
import sys
import json
import olefile
import re
from pathlib import Path

if sys.platform == 'win32':
    import codecs
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')

SOURCE_DIR = r"D:\Documentos\Centro\Umbanda\Curso de Umbanda"
OUTPUT_DIR = r"X:\Compilação\Catálogo da umbanda"

DOCUMENTS = [
    ("01", "01-historia-da-umbanda.doc", "01-Fundamentos", "Historia da Umbanda"),
    ("02", "02-o-que-e-umbanda.doc", "01-Fundamentos", "O que e Umbanda"),
    ("03", "03-outras-religioes-afro-brasileiras.doc", "01-Fundamentos", "Outras Religiões Afro-Brasileiras"),
    ("04", "04-os-orixas.doc", "02-Orixas", "Os Orixas"),
    ("05", "05-as-sete-linhas.doc", "02-Orixas", "As Sete Linhas"),
    ("06", "06-oxala.doc", "02-Orixas/Orixas-Maiores", "Oxala"),
    ("07", "07-yemanja.doc", "02-Orixas/Orixas-Maiores", "Iemanja"),
    ("08", "08-nana.doc", "02-Orixas/Orixas-Maiores", "Nana"),
    ("09", "09-oxum.doc", "02-Orixas/Orixas-Maiores", "Oxum"),
    ("10", "10-ogum.doc", "02-Orixas/Orixas-Maiores", "Ogum"),
    ("11", "11-xango.doc", "02-Orixas/Orixas-Maiores", "Xango"),
    ("12", "12-iansa.doc", "02-Orixas/Orixas-Maiores", "Iansa"),
    ("13", "13-oxossi.doc", "02-Orixas/Orixas-Menores", "Oxossi"),
    ("14", "14-obaluaie.doc", "02-Orixas/Orixas-Menores", "Obaluaiê"),
    ("15", "15-oxumare.doc", "02-Orixas/Orixas-Menores", "Oxumare"),
    ("16", "16-ibeiji.doc", "02-Orixas/Orixas-Menores", "Ibeiji"),
    ("17", "17-ossae.doc", "02-Orixas/Orixas-Menores", "Ossaie"),
    ("18", "18-ewa.doc", "02-Orixas/Orixas-Menores", "Ewa"),
    ("19", "19-oba.doc", "02-Orixas/Orixas-Menores", "Oba"),
    ("20", "20-logum-ede.doc", "02-Orixas/Orixas-Menores", "Logum Ede"),
    ("21", "21-exu.doc", "03-Entidades/Exus", "Exu"),
    ("22", "22-iroko-tempo-ifa-e-orumila.doc", "03-Entidades/Exus", "Iroko Tempo Ifa e Orumila"),
    ("23", "23-os-pretos-velhos.doc", "03-Entidades/Pretos-Velhos", "Os Pretos Velhos"),
    ("24", "24-os-caboclos.doc", "03-Entidades/Caboclos", "Os Caboclos"),
    ("25", "25-os-exus.doc", "03-Entidades/Exus", "Os Exus"),
    ("26", "26-classificacao_dos_exus.doc", "03-Entidades/Exus", "Classificacao dos Exus"),
    ("27", "27-as-criancas.doc", "03-Entidades/Outros", "As Criancias"),
    ("28", "28-boiadeiros.doc", "03-Entidades/Outros", "Boiadeiros"),
    ("29", "29-marinheiros.doc", "03-Entidades/Outros", "Marinheiros"),
    ("30", "30-os-ciganos.doc", "03-Entidades/Outros", "Os Ciganos"),
    ("31", "31-malandros.doc", "03-Entidades/Outros", "Malandros"),
    ("32", "32-baianos.doc", "03-Entidades/Outros", "Baianos"),
    ("33", "33-mentores-de-cura.doc", "03-Entidades/Outros", "Mentores de Cura"),
    ("34", "34-hierarquia.doc", "04-Hierarquia-Organizacao", "Hierarquia"),
    ("35", "35-pontos_vibracionais_do_terreiro.doc", "04-Hierarquia-Organizacao", "Pontos Vibracionais do Terreiro"),
    ("36", "36-cumprimentos-e-posturas.doc", "05-Praticas-Rituais/Vestuario", "Cumprimentos e Posturas"),
    ("37", "37-vestuario.doc", "05-Praticas-Rituais/Vestuario", "Vestuario"),
    ("38", "38-anjo_da_guarda.doc", "05-Praticas-Rituais/Elementos-Sagrados", "Anjo da Guarda"),
    ("39", "39-fios-de-conta.doc", "05-Praticas-Rituais/Elementos-Sagrados", "Fios de Conta"),
    ("40", "40-aguas.doc", "05-Praticas-Rituais/Elementos-Sagrados", "Aguas"),
    ("41", "41-banhos.doc", "05-Praticas-Rituais/Elementos-Sagrados", "Banhos"),
    ("42", "42-defumacao.doc", "05-Praticas-Rituais/Elementos-Sagrados", "Defumacao"),
    ("43", "43-ervas.doc", "05-Praticas-Rituais/Elementos-Sagrados", "Ervas"),
    ("44", "44-velas.doc", "05-Praticas-Rituais/Elementos-Sagrados", "Velas"),
    ("45", "45-fumo-e-bebidas.doc", "05-Praticas-Rituais/Elementos-Sagrados", "Fumo e Bebidas"),
    ("46", "46-pontos-cantados.doc", "05-Praticas-Rituais/Musica", "Pontos Cantados"),
    ("47", "47_-_atabaques.doc", "05-Praticas-Rituais/Musica", "Atabaques"),
]

TITLE_MAP = {
    "01": "Historia da Umbanda",
    "02": "O que e Umbanda",
    "03": "Outras Religiões Afro-Brasileiras",
    "04": "Os Orixas",
    "05": "As Sete Linhas",
    "06": "Oxala",
    "07": "Iemanja",
    "08": "Nana",
    "09": "Oxum",
    "10": "Ogum",
    "11": "Xango",
    "12": "Iansa",
    "13": "Oxossi",
    "14": "Obaluaiê",
    "15": "Oxumare",
    "16": "Ibeiji",
    "17": "Ossaie",
    "18": "Ewa",
    "19": "Oba",
    "20": "Logum Ede",
    "21": "Exu",
    "22": "Iroko - Tempo, Ifa e Orumila",
    "23": "Os Pretos Velhos",
    "24": "Os Caboclos",
    "25": "Os Exus",
    "26": "Classificacao dos Exus",
    "27": "As Criancias",
    "28": "Boiadeiros",
    "29": "Marinheiros",
    "30": "Os Ciganos",
    "31": "Malandros",
    "32": "Baianos",
    "33": "Mentores de Cura",
    "34": "Hierarquia",
    "35": "Pontos Vibracionais do Terreiro",
    "36": "Cumprimentos e Posturas",
    "37": "Vestuario",
    "38": "Anjo da Guarda",
    "39": "Fios de Conta",
    "40": "Aguas",
    "41": "Banhos",
    "42": "Defumacao",
    "43": "Ervas",
    "44": "Velas",
    "45": "Fumo e Bebidas",
    "46": "Pontos Cantados",
    "47": "Atabaques",
}

def extract_text_from_doc_ole(doc_path):
    try:
        if not olefile.isOleFile(doc_path):
            return None
            
        ole = olefile.OleFileIO(doc_path)
        
        if ole.exists('WordDocument'):
            word_stream = ole.openstream('WordDocument')
            word_data = word_stream.read()
            word_stream.close()
            
            text = extract_textFromWordData(word_data)
            ole.close()
            return text
        
        ole.close()
        return None
    except Exception as e:
        print(f"Erro ao processar {doc_path}: {e}")
        return None

def extract_textFromWordData(data):
    try:
        text = ""
        pos = 0
        length = len(data)
        
        while pos < length - 4:
            if data[pos:pos+2] == b'\x00\x00':
                size = int.from_bytes(data[pos+2:pos+4], 'little')
                if 1 < size < 10000 and pos + 4 + size <= length:
                    chunk = data[pos+4:pos+4+size]
                    try:
                        decoded = chunk.decode('utf-16-le', errors='ignore').replace('\x00', '')
                        if decoded.strip():
                            text += decoded + "\n"
                    except:
                        pass
                pos += 2
            else:
                pos += 1
        
        text = re.sub(r'\n\s*\n', '\n\n', text)
        text = re.sub(r'[^\x20-\x7E\n\r\t]', '', text)
        
        return text.strip()
    except Exception as e:
        return None

def create_html_page(title, content, num, category):
    formatted_content = format_content(content) if content else "<p>Conteudo nao disponivel.</p>"
    
    html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{num} - {title} - Curso de Umbanda</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
            min-height: 100vh;
            color: #eee;
            padding: 20px;
        }}
        .container {{ max-width: 900px; margin: 0 auto; }}
        header {{
            text-align: center;
            padding: 30px 0;
            border-bottom: 2px solid #c9a227;
            margin-bottom: 30px;
        }}
        h1 {{ font-size: 2em; color: #c9a227; margin-bottom: 10px; }}
        .num {{ color: #c9a227; }}
        .back-link {{
            display: inline-block;
            padding: 10px 20px;
            background: #c9a227;
            color: #1a1a2e;
            text-decoration: none;
            border-radius: 5px;
            margin-bottom: 20px;
            font-weight: bold;
        }}
        .back-link:hover {{ background: #e0c060; }}
        .content {{
            background: rgba(255,255,255,0.05);
            padding: 30px;
            border-radius: 10px;
            line-height: 1.8;
            text-align: justify;
            white-space: pre-wrap;
        }}
        .content h1, .content h2, .content h3 {{
            color: #c9a227;
            margin: 20px 0 10px 0;
        }}
        .content p {{ margin-bottom: 15px; }}
        .content ul, .content ol {{ margin-left: 30px; margin-bottom: 15px; }}
        footer {{
            text-align: center;
            padding: 30px;
            color: #666;
            margin-top: 30px;
        }}
    </style>
</head>
<body>
    <div class="container">
        <a href="../index.html" class="back-link">&larr; Voltar ao Catalogo</a>
        <header>
            <h1><span class="num">{num}</span> - {title}</h1>
        </header>
        <div class="content">
{formatted_content}
        </div>
        <footer>
            <p>☥ Curso de Umbanda</p>
        </footer>
    </div>
</body>
</html>"""
    return html

def format_content(text):
    if not text:
        return "<p>Conteudo nao disponivel.</p>"
    
    lines = text.split('\n')
    html_parts = []
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
        if line.isupper() and len(line) < 60:
            html_parts.append(f"<h3>{line}</h3>")
        elif line.startswith(('1.', '2.', '3.', '4.', '5.', '6.', '7.', '8.', '9.')):
            html_parts.append(f"<li>{line[3:].strip()}</li>")
        else:
            html_parts.append(f"<p>{line}</p>")
    
    return '\n'.join(html_parts)

def main():
    print("Iniciando extracao de conteudo...")
    
    db_data = {"documentos": []}
    processed = 0
    
    for num, filename, folder, title in DOCUMENTS:
        doc_path = os.path.join(SOURCE_DIR, filename)
        print(f"Processando: {num} - {title}...")
        
        text = extract_text_from_doc_ole(doc_path)
        
        if text and len(text) > 50:
            output_folder = os.path.join(OUTPUT_DIR, folder)
            os.makedirs(output_folder, exist_ok=True)
            
            html_page = create_html_page(title, text, num, folder)
            
            html_filename = f"{num}-{title}.html"
            html_filename = html_filename.replace(' ', '-').replace(',', '')
            html_path = os.path.join(output_folder, html_filename)
            
            with open(html_path, 'w', encoding='utf-8') as f:
                f.write(html_page)
            
            db_data["documentos"].append({
                "num": num,
                "titulo": title,
                "pasta": folder,
                "arquivo": filename,
                "html": f"{folder}/{html_filename}",
                "conteudo": text
            })
            
            print(f"  OK: {html_filename} ({len(text)} chars)")
            processed += 1
        else:
            print(f"  ERRO: Falha ao extrair texto")
    
    db_path = os.path.join(OUTPUT_DIR, "database.json")
    with open(db_path, 'w', encoding='utf-8') as f:
        json.dump(db_data, f, ensure_ascii=False, indent=2)
    
    print(f"\nBanco de dados salvo em: {db_path}")
    print(f"Total de documentos processados: {processed}/{len(DOCUMENTS)}")

if __name__ == "__main__":
    main()
