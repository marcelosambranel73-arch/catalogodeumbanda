import os
import subprocess
import shutil
import tempfile

SOURCE_DIR = r"D:\Documentos\Centro\Umbanda\Curso de Umbanda"
OUTPUT_DIR = r"y:\Compilação\Catálogo da umbanda"
LIBREOFFICE_EXE = r"C:\Program Files\LibreOffice\program\soffice.exe"

DOCUMENTS = [
    ("01", "01-historia-da-umbanda.doc", "01-Fundamentos", "Historia da Umbanda"),
    ("02", "02-o-que-e-umbanda.doc", "01-Fundamentos", "O que e Umbanda"),
    ("03", "03-outras-religioes-afro-brasileiras.doc", "01-Fundamentos", "Outras Religioes Afro-Brasileiras"),
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
    ("22", "22-iroko-tempo-ifa-e-orumila.doc", "03-Entidades/Exus", "Iroko - Tempo, Ifa e Orumila"),
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

def main():
    if not os.path.exists(LIBREOFFICE_EXE):
        print("Erro: LibreOffice não encontrado.")
        return

    temp_dir = tempfile.mkdtemp()
    print(f"Diretório temporário criado em: {temp_dir}")

    total = len(DOCUMENTS)
    for i, (num, filename, folder, title) in enumerate(DOCUMENTS, 1):
        source_doc = os.path.join(SOURCE_DIR, filename)
        if not os.path.exists(source_doc):
            print(f"Documento não encontrado: {source_doc}")
            continue
            
        print(f"[{i}/{total}] Convertendo {filename} para {folder}...")
        
        target_folder = os.path.join(OUTPUT_DIR, folder.replace('/', os.sep))
        os.makedirs(target_folder, exist_ok=True)
        
        cmd = f'"{LIBREOFFICE_EXE}" --headless --convert-to html "{source_doc}" --outdir "{temp_dir}"'
        subprocess.run(cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
        base_name = os.path.splitext(filename)[0]
        html_generated = os.path.join(temp_dir, f"{base_name}.html")
        
        final_html_name = f"{num}-{title.replace(' ', '-').replace(',', '')}.html"
        final_html_path = os.path.join(target_folder, final_html_name)
        
        if os.path.exists(html_generated):
            shutil.copy2(html_generated, final_html_path)
            
            for f in os.listdir(temp_dir):
                if f.startswith(f"{base_name}_html_") and (f.endswith(".png") or f.endswith(".jpg") or f.endswith(".gif") or f.endswith(".jpeg")):
                    src_img = os.path.join(temp_dir, f)
                    dst_img = os.path.join(target_folder, f)
                    shutil.copy2(src_img, dst_img)
                    print(f"  -> Imagem exportada: {f}")
        
        for f in os.listdir(temp_dir):
            os.remove(os.path.join(temp_dir, f))

    print("Conversão concluída. As imagens foram extraídas!")

if __name__ == "__main__":
    main()
