#!/usr/bin/env python3
"""
Convert USER_GUIDE.md to DOCX using Pandoc with proper TOC.
Author: Claude AI for SURIOTA
"""

import os
import re
import subprocess
import shutil
from pathlib import Path

# Paths
SCRIPT_DIR = Path(__file__).parent
PROJECT_DIR = SCRIPT_DIR.parent
MD_FILE = PROJECT_DIR / "docs" / "USER_GUIDE.md"
OUTPUT_DIR = PROJECT_DIR / "output"
OUTPUT_FILE = OUTPUT_DIR / "Panduan_Pengguna_Gateway_Config_App.docx"
TEMP_MD = OUTPUT_DIR / "temp_clean.md"

def clean_markdown_for_pandoc(content):
    """Clean markdown content for better Pandoc processing."""
    lines = content.split('\n')
    cleaned_lines = []
    skip_toc_table = False

    for line in lines:
        # Skip HTML tags
        if line.strip().startswith('<p align') or line.strip().startswith('</p>'):
            continue
        if line.strip().startswith('<h') or line.strip().startswith('</h'):
            continue
        if line.strip().startswith('<a href') or line.strip().startswith('</a>'):
            continue
        if line.strip().startswith('<img'):
            continue
        if line.strip().startswith('<strong>') or line.strip().startswith('</strong>'):
            continue

        # Skip the manual TOC table (we'll use Pandoc's TOC)
        if '## 📋 Daftar Isi' in line or '## Daftar Isi' in line:
            skip_toc_table = True
            continue
        if skip_toc_table:
            if line.strip().startswith('## ') and 'Daftar Isi' not in line:
                skip_toc_table = False
            elif line.strip().startswith('---'):
                skip_toc_table = False
                continue
            else:
                continue

        # Clean emojis from headings for cleaner TOC
        if line.startswith('## '):
            # Remove emojis but keep the text
            cleaned = re.sub(r'[📱📋🎯✨📦📥⚙️🔌📶💡❓📞🔗📡📊🌐☁️📈💾🔄⚡🔧📝📑🏠📤📁✅❌⚠️🔍💻🔒📌🛠️]', '', line)
            cleaned = cleaned.strip()
            # Remove extra spaces
            cleaned = re.sub(r'\s+', ' ', cleaned)
            cleaned_lines.append(cleaned)
            continue

        if line.startswith('### '):
            cleaned = re.sub(r'[📱📋🎯✨📦📥⚙️🔌📶💡❓📞🔗📡📊🌐☁️📈💾🔄⚡🔧📝📑🏠📤📁✅❌⚠️🔍💻🔒📌🛠️]', '', line)
            cleaned = cleaned.strip()
            cleaned = re.sub(r'\s+', ' ', cleaned)
            cleaned_lines.append(cleaned)
            continue

        # Fix image paths for Pandoc (relative to output directory)
        if '![' in line:
            # Convert relative paths
            line = line.replace('../assets/screenshots/', '../assets/screenshots/')
            line = line.replace('assets/screenshots/', '../assets/screenshots/')

        cleaned_lines.append(line)

    return '\n'.join(cleaned_lines)

def create_pandoc_metadata():
    """Create YAML metadata block for Pandoc."""
    return """---
title: "PANDUAN PENGGUNA"
subtitle: "Gateway Config App"
author: "PT Surya Inovasi Prioritas (SURIOTA)"
date: "Desember 2025"
subject: "User Guide"
keywords: [Gateway, Modbus, IIoT, MQTT, Configuration]
lang: id
toc: true
toc-depth: 3
toc-title: "DAFTAR ISI"
lof: true
lot: true
lof-title: "DAFTAR GAMBAR"
lot-title: "DAFTAR TABEL"
documentclass: report
papersize: a4
geometry:
  - margin=2.5cm
fontsize: 11pt
linestretch: 1.15
header-includes:
  - \\usepackage{fancyhdr}
  - \\pagestyle{fancy}
  - \\fancyhead[C]{SRT-MGATE-1210 User Guide Series}
  - \\fancyfoot[C]{PT Surya Inovasi Prioritas (SURIOTA) - Halaman \\thepage}
---

"""

def main():
    """Main conversion function using Pandoc."""
    print("=" * 60)
    print("Converting USER_GUIDE.md to DOCX using Pandoc")
    print("=" * 60)

    # Create output directory
    OUTPUT_DIR.mkdir(exist_ok=True)

    # Read markdown file
    print(f"Reading: {MD_FILE}")
    with open(MD_FILE, 'r', encoding='utf-8') as f:
        md_content = f.read()

    # Clean markdown
    print("Cleaning markdown...")
    cleaned_content = clean_markdown_for_pandoc(md_content)

    # Add metadata
    final_content = create_pandoc_metadata() + cleaned_content

    # Write temp file
    print(f"Writing temp file: {TEMP_MD}")
    with open(TEMP_MD, 'w', encoding='utf-8') as f:
        f.write(final_content)

    # Run Pandoc
    print("Running Pandoc...")

    # Change to project directory for correct image paths
    os.chdir(PROJECT_DIR)

    pandoc_cmd = [
        'pandoc',
        str(TEMP_MD),
        '-o', str(OUTPUT_FILE),
        '--toc',
        '--toc-depth=3',
        '--reference-doc=' + str(SCRIPT_DIR / 'reference.docx') if (SCRIPT_DIR / 'reference.docx').exists() else '',
        '--standalone',
        '--wrap=none',
        '-f', 'markdown+smart+pipe_tables+yaml_metadata_block',
        '-t', 'docx'
    ]

    # Remove empty arguments
    pandoc_cmd = [arg for arg in pandoc_cmd if arg]

    print(f"Command: {' '.join(pandoc_cmd)}")

    try:
        result = subprocess.run(
            pandoc_cmd,
            capture_output=True,
            text=True,
            check=True
        )
        print("Pandoc completed successfully!")
        if result.stdout:
            print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Pandoc error: {e}")
        if e.stderr:
            print(f"Stderr: {e.stderr}")
        return False

    # Clean up temp file
    if TEMP_MD.exists():
        TEMP_MD.unlink()
        print("Cleaned up temp file")

    print("=" * 60)
    print(f"Done! Output: {OUTPUT_FILE}")
    print("=" * 60)

    return True

if __name__ == "__main__":
    main()
