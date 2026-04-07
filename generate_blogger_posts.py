#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gera arquivos HTML individuais para cada post do Blogger
"""

import os
import re
from datetime import datetime


def clean_html(html_content):
    """Remove estilos e scripts e limpa o HTML"""
    content = re.sub(r"<style[\s\S]*?</style>", "", html_content)
    content = re.sub(r"<script[\s\S]*?</script>", "", content)
    content = re.sub(r"<meta[^>]*>", "", content)
    content = re.sub(r"<link[^>]*>", "", content)
    content = re.sub(r"<title>[^<]*</title>", "", content)
    content = re.sub(r"@page[^{]*{[^}]*}", "", content)
    content = re.sub(r'class="[^"]*"', "", content)
    content = re.sub(r'dir="ltr"', "", content)
    content = re.sub(r'text="#[^"]*"', "", content)
    content = re.sub(r'link="#[^"]*"', "", content)
    content = re.sub(r'vlink="#[^"]*"', "", content)
    content = re.sub(r'<font size="(\d+)"', r'<font size="\1"', content)
    return content


def extract_title(html_content):
    """Extrai o título do documento"""
    title_match = re.search(r"<title>([^<]*)</title>", html_content)
    if title_match:
        return title_match.group(1)
    return "Sem título"


def get_file_category(file_path):
    """Determina a categoria do documento"""
    if "01-Fundamentos" in file_path:
        return "Fundamentos"
    elif "02-Orixas" in file_path:
        return "Orixás"
    elif "03-Entidades" in file_path:
        return "Entidades"
    elif "04-Hierarquia" in file_path:
        return "Hierarquia"
    elif "05-Praticas" in file_path:
        return "Práticas Rituais"
    else:
        return "Geral"


def create_blogger_post_html(title, content, category, doc_num):
    """Cria HTML formatado para post do Blogger"""
    html = f"""<!-- Post {doc_num}: {title} -->
<!-- Categoria: {category} -->
<div class="post-umbanda">
<h2>{title}</h2>
<div class="content">
{content}
</div>
<div class="post-footer">
<p style="font-size: 12px; color: #888;">Categoria: {category} | Documento {doc_num:02d}</p>
</div>
</div>
"""
    return html


def main():
    base_path = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(base_path, "blogger-posts")
    os.makedirs(output_dir, exist_ok=True)

    documents = [
        ("01-Fundamentos/01-Historia-da-Umbanda.html", 1, "História da Umbanda"),
        ("01-Fundamentos/02-O-que-e-Umbanda.html", 2, "O que é Umbanda"),
        (
            "01-Fundamentos/03-Outras-Religioes-Afro-Brasileiras.html",
            3,
            "Outras Religiões Afro-Brasileiras",
        ),
        ("02-Orixas/04-Os-Orixas.html", 4, "Os Orixás"),
        ("02-Orixas/05-As-Sete-Linhas.html", 5, "As Sete Linhas"),
        ("02-Orixas/Orixas-Maiores/06-Oxala.html", 6, "Oxalá"),
        ("02-Orixas/Orixas-Maiores/07-Iemanja.html", 7, "Iemanjá"),
        ("02-Orixas/Orixas-Maiores/08-Nana.html", 8, "Nanã"),
        ("02-Orixas/Orixas-Maiores/09-Oxum.html", 9, "Oxum"),
        ("02-Orixas/Orixas-Maiores/10-Ogum.html", 10, "Ogum"),
        ("02-Orixas/Orixas-Maiores/11-Xango.html", 11, "Xangô"),
        ("02-Orixas/Orixas-Maiores/12-Iansa.html", 12, "Iansã"),
        ("02-Orixas/Orixas-Menores/13-Oxossi.html", 13, "Oxossi"),
        ("02-Orixas/Orixas-Menores/14-Obaluaiê.html", 14, "Obaluaiê"),
        ("02-Orixas/Orixas-Menores/15-Oxumare.html", 15, "Oxumaré"),
        ("02-Orixas/Orixas-Menores/16-Ibeiji.html", 16, "Ibeiji"),
        ("02-Orixas/Orixas-Menores/17-Ossaie.html", 17, "Ossãe"),
        ("02-Orixas/Orixas-Menores/18-Ewa.html", 18, "Ewá"),
        ("02-Orixas/Orixas-Menores/19-Oba.html", 19, "Oba"),
        ("02-Orixas/Orixas-Menores/20-Logum-Ede.html", 20, "Logun Edé"),
        ("03-Entidades/Exus/21-Exu.html", 21, "Exu"),
        (
            "03-Entidades/Exus/22-Iroko-Tempo-Ifa-e-Orumila.html",
            22,
            "Iroko - Tempo, Ifa e Orumila",
        ),
        ("03-Entidades/Pretos-Velhos/23-Os-Pretos-Velhos.html", 23, "Os Pretos Velhos"),
        ("03-Entidades/Caboclos/24-Os-Caboclos.html", 24, "Os Caboclos"),
        ("03-Entidades/Exus/25-Os-Exus.html", 25, "Os Exus"),
        (
            "03-Entidades/Exus/26-Classificacao-dos-Exus.html",
            26,
            "Classificação dos Exus",
        ),
        ("03-Entidades/Outros/27-As-Criancias.html", 27, "As Crianças"),
        ("03-Entidades/Outros/28-Boiadeiros.html", 28, "Boiadeiros"),
        ("03-Entidades/Outros/29-Marinheiros.html", 29, "Marinheiros"),
        ("03-Entidades/Outros/30-Os-Ciganos.html", 30, "Os Ciganos"),
        ("03-Entidades/Outros/31-Malandros.html", 31, "Malandros"),
        ("03-Entidades/Outros/32-Baianos.html", 32, "Baianos"),
        ("03-Entidades/Outros/33-Mentores-de-Cura.html", 33, "Mentores de Cura"),
        ("04-Hierarquia-Organizacao/34-Hierarquia.html", 34, "Hierarquia"),
        (
            "04-Hierarquia-Organizacao/35-Pontos-Vibracionais-do-Terreiro.html",
            35,
            "Pontos Vibracionais do Terreiro",
        ),
        (
            "05-Praticas-Rituais/Vestuario/36-Cumprimentos-e-Posturas.html",
            36,
            "Cumprimentos e Posturas",
        ),
        ("05-Praticas-Rituais/Vestuario/37-Vestuario.html", 37, "Vestuário"),
        (
            "05-Praticas-Rituais/Elementos-Sagrados/38-Anjo-da-Guarda.html",
            38,
            "Anjo da Guarda",
        ),
        (
            "05-Praticas-Rituais/Elementos-Sagrados/39-Fios-de-Conta.html",
            39,
            "Fios de Conta",
        ),
        ("05-Praticas-Rituais/Elementos-Sagrados/40-Aguas.html", 40, "Águas"),
        ("05-Praticas-Rituais/Elementos-Sagrados/41-Banhos.html", 41, "Banhos"),
        ("05-Praticas-Rituais/Elementos-Sagrados/42-Defumacao.html", 42, "Defumação"),
        ("05-Praticas-Rituais/Elementos-Sagrados/43-Ervas.html", 43, "Ervas"),
        ("05-Praticas-Rituais/Elementos-Sagrados/44-Velas.html", 44, "Velas"),
        (
            "05-Praticas-Rituais/Elementos-Sagrados/45-Fumo-e-Bebidas.html",
            45,
            "Fumo e Bebidas",
        ),
        ("05-Praticas-Rituais/Musica/46-Pontos-Cantados.html", 46, "Pontos Cantados"),
        ("05-Praticas-Rituais/Musica/47-Atabaques.html", 47, "Atabaques"),
    ]

    print("Gerando posts individuais para o Blogger...")

    all_posts = []

    for file_path, doc_num, title in documents:
        full_path = os.path.join(base_path, file_path)
        if os.path.exists(full_path):
            try:
                with open(full_path, "r", encoding="utf-8") as f:
                    html_content = f.read()

                category = get_file_category(file_path)
                clean_content = clean_html(html_content)

                post_html = create_blogger_post_html(
                    title, clean_content, category, doc_num
                )

                filename = f"{doc_num:02d}-{title.lower().replace(' ', '-').replace('ã', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u').replace('ô', 'o').replace('ê', 'e').replace('ç', 'c')}.html"
                filepath = os.path.join(output_dir, filename)

                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(post_html)

                all_posts.append((doc_num, title, filename))
                print(f"  OK {doc_num:02d} - {title}")
            except Exception as e:
                print(f"  ERRO {doc_num:02d} - {title}: {e}")

    index_html = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Posts do Blogger - Curso de Umbanda</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 800px; margin: 50px auto; padding: 20px; }
        h1 { color: #c9a227; }
        .post-list { list-style: none; padding: 0; }
        .post-list li { padding: 10px; margin: 5px 0; background: #f5f5f5; border-radius: 5px; }
        .post-list a { text-decoration: none; color: #333; }
        .post-list a:hover { color: #c9a227; }
    </style>
</head>
<body>
    <h1>Posts do Blogger - Curso de Umbanda</h1>
    <p>Copie o conteudo de cada arquivo e cole no editor do Blogger (modo HTML).</p>
    <ul class="post-list>
"""

    for doc_num, title, filename in all_posts:
        index_html += f'    <li><a href="{filename}">{doc_num:02d} - {title}</a></li>\n'

    index_html += """    </ul>
</body>
</html>"""

    with open(os.path.join(output_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(index_html)

    print(f"\nTotal: {len(all_posts)} posts gerados em: {output_dir}")
    print(
        "Para usar: Abra cada arquivo, copie o conteudo e cole no modo HTML do editor do Blogger"
    )


if __name__ == "__main__":
    main()
