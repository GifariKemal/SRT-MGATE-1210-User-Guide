#!/usr/bin/env python3
"""
Convert USER_GUIDE.md to DOCX with proper image sizing and page numbers.
Author: Claude AI for SURIOTA
"""

import os
import re
from pathlib import Path
from docx import Document
from docx.shared import Inches, Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
from docx.enum.style import WD_STYLE_TYPE
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn, nsmap
from docx.oxml import OxmlElement

# Paths
SCRIPT_DIR = Path(__file__).parent
PROJECT_DIR = SCRIPT_DIR.parent
MD_FILE = PROJECT_DIR / "docs" / "USER_GUIDE.md"
SCREENSHOTS_DIR = PROJECT_DIR / "assets" / "screenshots"
OUTPUT_DIR = PROJECT_DIR / "output"
OUTPUT_FILE = OUTPUT_DIR / "Panduan_Pengguna_Gateway_Config_App.docx"

# Document settings
IMAGE_WIDTH = Inches(4.5)  # Moderate size, not full page
PAGE_WIDTH = Inches(8.5)
PAGE_HEIGHT = Inches(11)
MARGIN = Inches(1)

def create_element(name):
    return OxmlElement(name)

def create_attribute(element, name, value):
    element.set(qn(name), value)

def add_page_number(run):
    """Add page number field to a run."""
    fldChar1 = create_element('w:fldChar')
    create_attribute(fldChar1, 'w:fldCharType', 'begin')

    instrText = create_element('w:instrText')
    create_attribute(instrText, 'xml:space', 'preserve')
    instrText.text = "PAGE"

    fldChar2 = create_element('w:fldChar')
    create_attribute(fldChar2, 'w:fldCharType', 'end')

    run._r.append(fldChar1)
    run._r.append(instrText)
    run._r.append(fldChar2)

def setup_header_footer(doc):
    """Add header with document series and footer with author and page numbers."""
    section = doc.sections[0]

    # === HEADER ===
    header = section.header
    header.is_linked_to_previous = False

    # Header paragraph - Document Series
    p = header.paragraphs[0] if header.paragraphs else header.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER

    run = p.add_run("SRT-MGATE-1210 User Guide Series")
    run.font.size = Pt(10)
    run.font.name = "Calibri"
    run.font.color.rgb = RGBColor(0, 102, 153)
    run.font.bold = True

    # Add separator line
    p2 = header.add_paragraph()
    p2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run2 = p2.add_run("Panduan Pengguna Gateway Config App v1.0")
    run2.font.size = Pt(9)
    run2.font.name = "Calibri"
    run2.font.color.rgb = RGBColor(128, 128, 128)
    run2.font.italic = True

    # === FOOTER ===
    footer = section.footer
    footer.is_linked_to_previous = False

    # Footer line 1 - Company info
    p = footer.paragraphs[0] if footer.paragraphs else footer.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER

    run = p.add_run("PT Surya Inovasi Prioritas (SURIOTA)")
    run.font.size = Pt(9)
    run.font.name = "Calibri"
    run.font.color.rgb = RGBColor(0, 102, 153)
    run.font.bold = True

    # Footer line 2 - Page number
    p2 = footer.add_paragraph()
    p2.alignment = WD_ALIGN_PARAGRAPH.CENTER

    run2 = p2.add_run("Halaman ")
    run2.font.size = Pt(9)
    run2.font.name = "Calibri"
    run2.font.color.rgb = RGBColor(100, 100, 100)

    # Add page number field
    add_page_number(p2.add_run())

    run3 = p2.add_run(" | www.suriota.com")
    run3.font.size = Pt(9)
    run3.font.name = "Calibri"
    run3.font.color.rgb = RGBColor(100, 100, 100)

def setup_styles(doc):
    """Setup document styles."""
    styles = doc.styles

    # Title style
    title_style = styles['Title']
    title_style.font.name = 'Calibri'
    title_style.font.size = Pt(28)
    title_style.font.bold = True
    title_style.font.color.rgb = RGBColor(0, 102, 153)

    # Heading 1
    h1 = styles['Heading 1']
    h1.font.name = 'Calibri'
    h1.font.size = Pt(18)
    h1.font.bold = True
    h1.font.color.rgb = RGBColor(0, 102, 153)

    # Heading 2
    h2 = styles['Heading 2']
    h2.font.name = 'Calibri'
    h2.font.size = Pt(14)
    h2.font.bold = True
    h2.font.color.rgb = RGBColor(0, 128, 128)

    # Heading 3
    h3 = styles['Heading 3']
    h3.font.name = 'Calibri'
    h3.font.size = Pt(12)
    h3.font.bold = True

    # Normal text
    normal = styles['Normal']
    normal.font.name = 'Calibri'
    normal.font.size = Pt(11)

    return styles

def add_cover_page(doc):
    """Add professional cover page."""
    # Title
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("\n\n\n\n")

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("PANDUAN PENGGUNA")
    run.font.size = Pt(36)
    run.font.bold = True
    run.font.color.rgb = RGBColor(0, 102, 153)
    run.font.name = "Calibri"

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("Gateway Config App")
    run.font.size = Pt(24)
    run.font.name = "Calibri"
    run.font.color.rgb = RGBColor(0, 128, 128)

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("\n\nAplikasi Konfigurasi untuk\nSRT-MGATE-1210 Modbus Gateway IIoT")
    run.font.size = Pt(14)
    run.font.name = "Calibri"

    # Add spacing
    for _ in range(8):
        doc.add_paragraph()

    # Version info
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("Versi Dokumen: 1.0.0")
    run.font.size = Pt(12)
    run.font.name = "Calibri"

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("Desember 2025")
    run.font.size = Pt(12)
    run.font.name = "Calibri"

    # Company info
    for _ in range(4):
        doc.add_paragraph()

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("PT Surya Inovasi Prioritas (SURIOTA)")
    run.font.size = Pt(14)
    run.font.bold = True
    run.font.name = "Calibri"
    run.font.color.rgb = RGBColor(0, 102, 153)

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("www.suriota.com")
    run.font.size = Pt(11)
    run.font.name = "Calibri"

    # Page break after cover
    doc.add_page_break()

def add_table_of_contents(doc):
    """Add table of contents page."""
    p = doc.add_heading("Daftar Isi", level=1)

    toc_items = [
        ("1.", "Tentang Aplikasi", "Pengenalan Gateway Config App"),
        ("2.", "Persiapan Sebelum Memulai", "Kebutuhan dan instalasi"),
        ("3.", "Menghubungkan ke Gateway", "Koneksi Bluetooth ke perangkat"),
        ("4.", "Dashboard Utama", "Navigasi dan menu utama"),
        ("5.", "Konfigurasi Device (Sensor)", "Menambah dan mengatur sensor"),
        ("6.", "Konfigurasi Modbus", "Mengatur register data"),
        ("7.", "Konfigurasi Server", "Pengaturan jaringan dan MQTT"),
        ("8.", "Status & Monitoring", "Melihat status gateway"),
        ("9.", "Streaming Data", "Monitoring data real-time"),
        ("10.", "Pengaturan Aplikasi", "Settings dan informasi"),
        ("11.", "Troubleshooting", "Solusi masalah umum"),
        ("12.", "Referensi", "Link dan kontak support"),
    ]

    # Create TOC table
    table = doc.add_table(rows=1, cols=3)
    table.style = 'Table Grid'

    # Header row
    header_cells = table.rows[0].cells
    header_cells[0].text = "No"
    header_cells[1].text = "Bagian"
    header_cells[2].text = "Deskripsi"

    for cell in header_cells:
        cell.paragraphs[0].runs[0].font.bold = True
        cell.paragraphs[0].runs[0].font.size = Pt(11)

    # Content rows
    for num, title, desc in toc_items:
        row = table.add_row()
        row.cells[0].text = num
        row.cells[1].text = title
        row.cells[2].text = desc

    doc.add_paragraph()
    doc.add_page_break()

def find_image(image_name):
    """Find image file in screenshots directory."""
    # Clean the image name
    image_name = image_name.strip()

    # Try exact match first
    image_path = SCREENSHOTS_DIR / image_name
    if image_path.exists():
        return image_path

    # Try with URL decoding
    import urllib.parse
    decoded_name = urllib.parse.unquote(image_name)
    image_path = SCREENSHOTS_DIR / decoded_name
    if image_path.exists():
        return image_path

    # Search for partial match
    for f in SCREENSHOTS_DIR.glob("*.jpeg"):
        if image_name in f.name or decoded_name in f.name:
            return f

    for f in SCREENSHOTS_DIR.glob("*.jpg"):
        if image_name in f.name or decoded_name in f.name:
            return f

    return None

def add_image(doc, image_path, caption=None):
    """Add image with caption."""
    if not image_path or not Path(image_path).exists():
        print(f"Warning: Image not found: {image_path}")
        return

    # Add image paragraph
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run()

    try:
        run.add_picture(str(image_path), width=IMAGE_WIDTH)
    except Exception as e:
        print(f"Error adding image {image_path}: {e}")
        return

    # Add caption if provided
    if caption:
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run(caption)
        run.font.size = Pt(10)
        run.font.italic = True
        run.font.color.rgb = RGBColor(100, 100, 100)

    # Add small spacing after image
    doc.add_paragraph()

def parse_table(lines):
    """Parse markdown table into rows."""
    rows = []
    for line in lines:
        line = line.strip()
        if line.startswith('|') and line.endswith('|'):
            # Remove outer pipes and split
            cells = [cell.strip() for cell in line[1:-1].split('|')]
            # Skip separator rows
            if not all(set(cell) <= set('-: ') for cell in cells):
                rows.append(cells)
    return rows

def add_table(doc, rows):
    """Add table to document."""
    if not rows:
        return

    num_cols = len(rows[0])
    table = doc.add_table(rows=len(rows), cols=num_cols)
    table.style = 'Table Grid'

    for i, row_data in enumerate(rows):
        row = table.rows[i]
        for j, cell_text in enumerate(row_data):
            if j < len(row.cells):
                # Clean cell text (remove markdown links, bold, etc.)
                clean_text = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', cell_text)
                clean_text = re.sub(r'\*\*([^*]+)\*\*', r'\1', clean_text)
                clean_text = re.sub(r'`([^`]+)`', r'\1', clean_text)
                row.cells[j].text = clean_text

                # Bold first row (header)
                if i == 0:
                    for para in row.cells[j].paragraphs:
                        for run in para.runs:
                            run.font.bold = True
                            run.font.size = Pt(10)
                else:
                    for para in row.cells[j].paragraphs:
                        for run in para.runs:
                            run.font.size = Pt(10)

    doc.add_paragraph()

def process_markdown(doc, md_content):
    """Process markdown content and add to document."""
    lines = md_content.split('\n')
    i = 0
    current_section = ""
    in_code_block = False
    code_content = []
    table_lines = []
    in_table = False

    while i < len(lines):
        line = lines[i]

        # Skip HTML alignment tags
        if line.strip().startswith('<p align') or line.strip().startswith('</p>') or \
           line.strip().startswith('<h') or line.strip().startswith('</h') or \
           line.strip().startswith('<a href') or line.strip().startswith('</a>'):
            i += 1
            continue

        # Skip empty separator lines
        if line.strip() == '---':
            doc.add_paragraph()
            i += 1
            continue

        # Code blocks
        if line.strip().startswith('```'):
            if in_code_block:
                # End code block
                p = doc.add_paragraph()
                run = p.add_run('\n'.join(code_content))
                run.font.name = 'Consolas'
                run.font.size = Pt(9)
                code_content = []
                in_code_block = False
            else:
                in_code_block = True
            i += 1
            continue

        if in_code_block:
            code_content.append(line)
            i += 1
            continue

        # Tables
        if line.strip().startswith('|'):
            if not in_table:
                in_table = True
                table_lines = []
            table_lines.append(line)
            i += 1
            continue
        elif in_table:
            # End of table
            rows = parse_table(table_lines)
            add_table(doc, rows)
            in_table = False
            table_lines = []
            # Don't increment i, process current line
            continue

        # Headings
        if line.startswith('## '):
            title = line[3:].strip()
            # Remove emojis and clean
            title = re.sub(r'[^\w\s\.\-\(\)&]', '', title).strip()
            doc.add_heading(title, level=1)
            current_section = title
            i += 1
            continue

        if line.startswith('### '):
            title = line[4:].strip()
            title = re.sub(r'[^\w\s\.\-\(\)&?]', '', title).strip()
            doc.add_heading(title, level=2)
            i += 1
            continue

        if line.startswith('#### '):
            title = line[5:].strip()
            title = re.sub(r'[^\w\s\.\-\(\)&?:]', '', title).strip()
            doc.add_heading(title, level=3)
            i += 1
            continue

        # Images
        img_match = re.search(r'!\[([^\]]*)\]\(([^)]+)\)', line)
        if img_match:
            caption = img_match.group(1)
            img_path = img_match.group(2)

            # Extract filename from path
            if '../assets/screenshots/' in img_path:
                img_name = img_path.replace('../assets/screenshots/', '')
            elif 'assets/screenshots/' in img_path:
                img_name = img_path.replace('assets/screenshots/', '')
            else:
                img_name = os.path.basename(img_path)

            # URL decode
            import urllib.parse
            img_name = urllib.parse.unquote(img_name)

            # Find and add image
            image_file = find_image(img_name)
            if image_file:
                add_image(doc, image_file, caption if caption else None)
            else:
                print(f"Image not found: {img_name}")

            i += 1
            continue

        # Bold text and lists
        if line.strip():
            # Clean markdown formatting
            text = line.strip()
            text = re.sub(r'\*\*([^*]+)\*\*', r'\1', text)
            text = re.sub(r'`([^`]+)`', r'\1', text)
            text = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', text)

            # Handle bullet points
            if text.startswith('- ') or text.startswith('* '):
                p = doc.add_paragraph(text[2:], style='List Bullet')
            elif re.match(r'^\d+\.\s', text):
                # Numbered list
                num_text = re.sub(r'^\d+\.\s*', '', text)
                p = doc.add_paragraph(num_text, style='List Number')
            elif text.startswith('> '):
                # Quote/Note
                p = doc.add_paragraph()
                run = p.add_run(text[2:])
                run.font.italic = True
                run.font.color.rgb = RGBColor(100, 100, 100)
            else:
                p = doc.add_paragraph(text)

        i += 1

    # Handle any remaining table
    if in_table and table_lines:
        rows = parse_table(table_lines)
        add_table(doc, rows)

def add_footer_info(doc):
    """Add document footer information."""
    doc.add_page_break()

    p = doc.add_heading("Informasi Dokumen", level=1)

    p = doc.add_paragraph()
    p.add_run("Judul: ").bold = True
    p.add_run("Panduan Pengguna Gateway Config App")

    p = doc.add_paragraph()
    p.add_run("Versi: ").bold = True
    p.add_run("1.0.0")

    p = doc.add_paragraph()
    p.add_run("Tanggal: ").bold = True
    p.add_run("Desember 2025")

    p = doc.add_paragraph()
    p.add_run("Penulis: ").bold = True
    p.add_run("Tim Dokumentasi SURIOTA")

    p = doc.add_paragraph()
    p.add_run("Dibantu oleh: ").bold = True
    p.add_run("Claude AI (Anthropic)")

    doc.add_paragraph()

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("Copyright 2025 PT Surya Inovasi Prioritas (SURIOTA)")
    run.font.size = Pt(10)

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("www.suriota.com | support@suriota.com")
    run.font.size = Pt(10)

def main():
    """Main conversion function."""
    print("=" * 60)
    print("Converting USER_GUIDE.md to DOCX")
    print("=" * 60)

    # Create output directory
    OUTPUT_DIR.mkdir(exist_ok=True)

    # Read markdown file
    print(f"Reading: {MD_FILE}")
    with open(MD_FILE, 'r', encoding='utf-8') as f:
        md_content = f.read()

    # Create document
    print("Creating document...")
    doc = Document()

    # Setup page margins
    section = doc.sections[0]
    section.page_width = PAGE_WIDTH
    section.page_height = PAGE_HEIGHT
    section.left_margin = MARGIN
    section.right_margin = MARGIN
    section.top_margin = MARGIN
    section.bottom_margin = MARGIN

    # Setup styles
    setup_styles(doc)

    # Setup header and footer (with page numbers)
    setup_header_footer(doc)

    # Add cover page
    print("Adding cover page...")
    add_cover_page(doc)

    # Add table of contents
    print("Adding table of contents...")
    add_table_of_contents(doc)

    # Process markdown content
    print("Processing content...")
    process_markdown(doc, md_content)

    # Add footer info
    print("Adding document info...")
    add_footer_info(doc)

    # Save document
    print(f"Saving: {OUTPUT_FILE}")
    doc.save(OUTPUT_FILE)

    print("=" * 60)
    print(f"Done! Output: {OUTPUT_FILE}")
    print("=" * 60)

if __name__ == "__main__":
    main()
