#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para copiar imagens para a pasta app
"""

import os
import shutil

base_path = os.path.dirname(os.path.abspath(__file__))
app_path = os.path.join(base_path, "app")
img_path = os.path.join(app_path, "images")

os.makedirs(img_path, exist_ok=True)

image_extensions = [".png", ".jpg", ".jpeg", ".gif"]

print("Copiando imagens...")

for root, dirs, files in os.walk(base_path):
    if "app" in root:
        continue

    for file in files:
        ext = os.path.splitext(file)[1].lower()
        if ext in image_extensions:
            src = os.path.join(root, file)
            dst = os.path.join(img_path, file)

            if not os.path.exists(dst):
                try:
                    shutil.copy2(src, dst)
                    print(f"  OK: {file}")
                except Exception as e:
                    print(f"  ERRO: {file} - {e}")

print(f"\nImagens copiadas para: {img_path}")
print("Total de imagens:", len(os.listdir(img_path)))
