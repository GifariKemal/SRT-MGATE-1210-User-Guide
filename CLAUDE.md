# CLAUDE.md - AI Assistant Guide

**Repository**: SRT-MGATE-1210 User Guide Documentation
**Last Updated**: November 30, 2025
**Version**: 1.0

---

## Table of Contents

1. [Repository Overview](#repository-overview)
2. [Codebase Structure](#codebase-structure)
3. [File Descriptions](#file-descriptions)
4. [Development Workflows](#development-workflows)
5. [Key Conventions](#key-conventions)
6. [Documentation Standards](#documentation-standards)
7. [Python Script Guidelines](#python-script-guidelines)
8. [Common Tasks](#common-tasks)
9. [Related Repositories](#related-repositories)
10. [Important Notes](#important-notes)

---

## Repository Overview

### Purpose

This repository contains **user documentation** for the **SRT-MGATE-1210 Industrial IoT Gateway** and its companion **Gateway Config App** (mobile application). The documentation helps end-users configure and operate the gateway system.

### Technology Stack

- **Documentation Format**: Markdown (.md), Microsoft Word (.docx)
- **Document Generation**: Python 3.x with `python-docx` library
- **Target Audience**: End-users, technicians, and field operators
- **Languages**: Indonesian (primary), English (secondary)

### Key Products Documented

1. **SRT-MGATE-1210 Gateway** - Industrial IoT gateway device
   - Modbus RTU/TCP protocol support
   - MQTT and HTTP cloud connectivity
   - WiFi and Ethernet network interfaces
   - BLE (Bluetooth Low Energy) configuration interface

2. **Gateway Config App** - Mobile application (Flutter-based)
   - Android 5.0+ and iOS 12+ support
   - BLE device scanning and pairing
   - Gateway provisioning and configuration
   - Backup/restore functionality
   - OTA firmware updates

---

## Codebase Structure

```
SRT-MGATE-1210-User-Guide/
├── .git/                              # Git repository metadata
├── USER_GUIDE_CLEAN.md                # Clean Indonesian user guide
├── USER_GUIDE_MOBILE_APP.md           # Technical English user guide
├── generate_user_guide_docx.py        # Python script to generate Word docs
└── Panduan_Pengguna_Gateway_Config_App.docx  # Generated Word document
```

### File Organization

- **Root Directory**: All documentation files are stored at the root level
- **No Subdirectories**: Simple flat structure for easy access
- **Generated Files**: Word documents are generated from Python script

---

## File Descriptions

### 1. `USER_GUIDE_CLEAN.md`

**Location**: `/home/user/SRT-MGATE-1210-User-Guide/USER_GUIDE_CLEAN.md`

**Purpose**: Primary Indonesian-language user guide with comprehensive end-user instructions

**Key Sections**:
- Document metadata (version 1.0, app version 1.0.0)
- 16 main sections covering complete user journey
- Installation and setup instructions
- BLE connection procedures
- Device configuration (Modbus RTU/TCP)
- Server configuration (MQTT/HTTP)
- Troubleshooting and FAQ

**Characteristics**:
- User-friendly language (non-technical)
- Step-by-step instructions with numbered lists
- Tables for parameter reference
- Example values and use cases

**Target Audience**: Indonesian-speaking end-users without technical background

---

### 2. `USER_GUIDE_MOBILE_APP.md`

**Location**: `/home/user/SRT-MGATE-1210-User-Guide/USER_GUIDE_MOBILE_APP.md`

**Purpose**: Technical English-language documentation with developer-friendly details

**Key Sections**:
- App architecture and features
- BLE service detection
- Network configuration (DHCP/Static IP)
- Modbus configuration with 30+ data types
- MQTT topic customization
- JSON payload examples
- Technical appendices

**Characteristics**:
- More technical terminology
- Code examples and JSON payloads
- Detailed data type specifications
- Source code references (GitHub links)
- Comprehensive FAQ with technical answers

**Target Audience**: Developers, integrators, and technical users

**Special Features**:
- MQTT payload examples (Section 16.2)
- Complete data type catalog (INT16, FLOAT32_BE, etc.)
- Endianness explanations (BE/LE/BS)
- Interval unit conversions (ms/s/m)

---

### 3. `generate_user_guide_docx.py`

**Location**: `/home/user/SRT-MGATE-1210-User-Guide/generate_user_guide_docx.py`

**Purpose**: Python script to generate professionally styled Word documents from markdown content

**Key Functions**:

| Function | Purpose |
|----------|---------|
| `create_element()` | Create OxmlElement for Word formatting |
| `add_page_number()` | Add page numbering to document |
| `set_cell_shading()` | Apply background colors to table cells |
| `setup_styles()` | Configure document styles (headings, fonts) |
| `add_header_footer()` | Add headers and footers with branding |
| `add_cover_page()` | Generate professional cover page |
| `add_styled_table()` | Create formatted tables with headers |
| `add_image_with_caption()` | Insert images with captions |
| `add_note_box()` | Create highlighted info/warning boxes |
| `add_section_X()` | Generate specific documentation sections |

**Configuration Variables**:

```python
# File paths (currently Windows-specific)
IMAGE_FOLDER = r"C:\Users\Administrator\Downloads\UI"
OUTPUT_FILE = r"C:\...\Panduan_Pengguna_Gateway_Config_App.docx"

# Document metadata
DOC_VERSION = "1.0"
APP_VERSION = "1.0.0"
DOC_DATE = "30 November 2025"
DOC_AUTHOR = "Tim Dokumentasi SURIOTA"
DOC_COMPANY = "PT SURIOTA Technology Indonesia"

# SURIOTA brand colors
PRIMARY_COLOR = RGBColor(0x3D, 0x7C, 0x72)  # Teal green
SECONDARY_COLOR = RGBColor(0x2C, 0x5C, 0x54)  # Dark teal
```

**Dependencies**:
- `python-docx` - Document generation
- Standard library: `os`, `datetime`

**Execution**: `python generate_user_guide_docx.py`

---

### 4. `Panduan_Pengguna_Gateway_Config_App.docx`

**Location**: `/home/user/SRT-MGATE-1210-User-Guide/Panduan_Pengguna_Gateway_Config_App.docx`

**Purpose**: Generated Word document for professional distribution

**Characteristics**:
- Professional styling with SURIOTA branding
- Cover page with metadata
- Table of contents with page numbers
- Headers and footers
- Styled tables with color coding
- Image placeholders with captions
- Note boxes for warnings/tips

**Use Cases**:
- Print documentation
- PDF conversion for distribution
- Official documentation release

---

## Development Workflows

### Workflow 1: Update Documentation Content

**When to Use**: Updating user instructions, adding new features, fixing errors

**Steps**:
1. Identify which file to update:
   - `USER_GUIDE_CLEAN.md` for Indonesian user-facing changes
   - `USER_GUIDE_MOBILE_APP.md` for technical/English changes
2. Edit the markdown file using the Edit tool
3. Maintain consistent formatting:
   - Use heading hierarchy (# → ## → ###)
   - Keep numbered lists for procedures
   - Use tables for parameter reference
   - Add examples where helpful
4. Test markdown rendering (if possible)
5. Commit changes with descriptive message

**Example Commit Message**:
```
docs: update BLE connection timeout from 5 to 10 minutes

- Update section 5.1 in USER_GUIDE_CLEAN.md
- Clarify timeout behavior in troubleshooting section
```

---

### Workflow 2: Generate Word Document

**When to Use**: Creating distributable Word document from markdown

**Prerequisites**:
- Python 3.x installed
- `python-docx` library installed
- UI images available (for screenshots)

**Steps**:
1. Update configuration in `generate_user_guide_docx.py`:
   - Set correct `IMAGE_FOLDER` path
   - Set desired `OUTPUT_FILE` path
   - Update metadata (version, date, author)
2. Place UI screenshots in IMAGE_FOLDER
3. Run: `python generate_user_guide_docx.py`
4. Review generated `.docx` file
5. Convert to PDF if needed

**Important Notes**:
- Script currently has hardcoded Windows paths
- Images are optional (script continues if not found)
- Generated file includes SURIOTA branding

---

### Workflow 3: Synchronize Indonesian and English Versions

**When to Use**: After major updates to ensure consistency

**Steps**:
1. Identify sections that differ between versions
2. Update content in both files:
   - Translate new content if adding to one version
   - Ensure technical accuracy is consistent
   - Maintain version-specific formatting
3. Verify section numbers align
4. Update metadata (version, date) in both files
5. Commit both files together

**Example Commit Message**:
```
docs: add logging configuration section to both guides

- Add section 10 to USER_GUIDE_CLEAN.md (Indonesian)
- Add section 10 to USER_GUIDE_MOBILE_APP.md (English)
- Update table of contents in both files
```

---

### Workflow 4: Version Release

**When to Use**: Releasing new documentation version

**Steps**:
1. Update version numbers in all files:
   - Document Version in markdown files
   - App Version (if app was updated)
   - DOC_VERSION in Python script
2. Update "Last Updated" dates
3. Update CHANGELOG (if exists) or commit message
4. Generate new Word document
5. Tag release in git: `git tag v1.1`
6. Push changes and tag

---

## Key Conventions

### Markdown Formatting

#### Headers
- **Level 1 (`#`)**: Main sections (1. Pendahuluan, 2. Persyaratan Sistem)
- **Level 2 (`##`)**: Subsections (1.1, 1.2)
- **Level 3 (`###`)**: Sub-subsections (1.1.1, procedural steps)

#### Lists
- **Numbered Lists**: For sequential procedures, steps
- **Bullet Lists**: For feature lists, non-sequential items
- **Tables**: For parameters, specifications, comparisons

#### Tables

**Standard Format**:
```markdown
| Parameter | Deskripsi | Contoh |
|-----------|-----------|--------|
| Device Name | Nama identifikasi | "Sensor_Suhu" |
```

**Alignment**: Left-aligned for text, keep columns consistent

#### Code Blocks

```markdown
```json
{
  "device_id": "SRT-MGATE-001",
  "data": { ... }
}
\```
```

Use language identifiers: `json`, `bash`, `python`

---

### Naming Conventions

#### File Names
- **Pattern**: `{CONTENT_TYPE}_{LANGUAGE}_{VARIANT}.{ext}`
- **Examples**:
  - `USER_GUIDE_CLEAN.md` - Clean version
  - `USER_GUIDE_MOBILE_APP.md` - App-focused
  - `Panduan_Pengguna_Gateway_Config_App.docx` - Indonesian Word doc

#### Section Numbering
- **Format**: `{number}. {Title}` (e.g., `1. Pendahuluan`)
- **Subsections**: `{number}.{sub}` (e.g., `1.1 Tentang Panduan Ini`)
- **Consistency**: Must match across languages

#### Image Naming
- **Pattern**: Timestamp-based (`06.13.24.jpeg`, `06.13.23 (1).jpeg`)
- **Captions**: `Gambar {section}.{number} - {Description}`

---

### Documentation Language Standards

#### Indonesian Version (`USER_GUIDE_CLEAN.md`)

**Tone**: Friendly, accessible, non-technical

**Key Phrases**:
- "Tekan tombol..." (Press button...)
- "Pastikan..." (Make sure...)
- "Tunggu hingga..." (Wait until...)
- "Anda akan melihat..." (You will see...)

**Avoid**: Technical jargon, acronyms without explanation

**Example**:
```markdown
✓ Tekan tombol Scan untuk memulai pencarian perangkat
✗ Initiate BLE scan procedure to enumerate nearby peripherals
```

---

#### English Version (`USER_GUIDE_MOBILE_APP.md`)

**Tone**: Technical, precise, developer-friendly

**Key Phrases**:
- "Dynamic BLE Service Detection"
- "Subscribe to topic..."
- "Configure endpoint..."
- "Execute command..."

**Include**: Technical details, JSON examples, source code references

**Example**:
```markdown
✓ Subscribe to the MQTT topic using mosquitto_sub:
   mosquitto_sub -h broker.hivemq.com -p 1883 -t "topic"

✗ Dengarkan data dari broker menggunakan program khusus
```

---

### Technical Terminology

#### Consistent Terms Across Languages

| English | Indonesian | Notes |
|---------|-----------|-------|
| Gateway | Gateway | No translation |
| Bluetooth | Bluetooth | No translation |
| Scan | Scan | Keep as-is |
| Connect | Hubungkan / Terhubung | Context-dependent |
| Device | Perangkat | Always translate |
| Configuration | Konfigurasi | Always translate |
| Register | Register | No translation (Modbus term) |
| Slave ID | Slave ID | No translation |
| Modbus RTU | Modbus RTU | No translation |
| MQTT Broker | MQTT Broker / Server MQTT | Both acceptable |
| Topic | Topic | No translation |
| Big Endian | Big Endian (BE) | Keep abbreviation |
| Little Endian | Little Endian (LE) | Keep abbreviation |

---

### Version Numbering

**Format**: `MAJOR.MINOR`

**Examples**:
- `1.0` - Initial release
- `1.1` - Minor update (new sections, clarifications)
- `2.0` - Major update (restructure, new app version)

**App Version Format**: `MAJOR.MINOR.PATCH` (e.g., `1.0.0`)

---

## Documentation Standards

### Section Structure

Each major section should follow this pattern:

```markdown
## {Number}. {Section Title}

{Brief introduction paragraph}

### {Number}.{Sub} {Subsection Title}

{Content with steps, tables, or explanations}

{Optional: Images, code blocks, note boxes}
```

---

### Writing Steps/Procedures

**Format**:
```markdown
1. First step
2. Second step
3. Third step
   - Sub-bullet if needed
   - Additional detail
```

**Guidelines**:
- Use imperative mood ("Tekan", "Pilih", "Isi")
- One action per step
- Include expected outcomes
- Add screenshots after complex steps

---

### Creating Tables

#### Parameter Tables

```markdown
| Parameter | Deskripsi | Contoh |
|-----------|-----------|--------|
| Device Name | Nama untuk identifikasi | Sensor_Suhu_Ruang1 |
| Slave ID | Alamat perangkat (1-247) | 1 |
```

#### Comparison Tables

```markdown
| Feature | Option 1 | Option 2 |
|---------|----------|----------|
| Speed | Fast | Slow |
| Cost | High | Low |
```

---

### Adding Examples

Always provide **realistic examples** for technical parameters:

**Good**:
```markdown
- MQTT Broker: broker.hivemq.com
- Topic: v1/devices/me/telemetry/gwsrt
- Interval: 5s (5 seconds)
```

**Bad**:
```markdown
- MQTT Broker: [your broker here]
- Topic: [topic name]
- Interval: [value]
```

---

### Note Boxes and Warnings

Use special formatting for important information:

**Info/Tips**:
```markdown
> **Tips:** Proses pencarian biasanya memakan waktu 5-10 detik
```

**Warnings**:
```markdown
> **Peringatan:** Jangan matikan gateway selama proses update!
```

**Notes**:
```markdown
> **Catatan:** Jika izin ditolak, aktifkan melalui Settings
```

---

## Python Script Guidelines

### Modifying `generate_user_guide_docx.py`

#### Common Modifications

1. **Update Paths** (most common):
```python
# Change these for your environment
IMAGE_FOLDER = r"/path/to/images"
OUTPUT_FILE = r"/path/to/output.docx"
```

2. **Update Metadata**:
```python
DOC_VERSION = "1.1"  # Increment version
APP_VERSION = "1.0.1"  # Match app version
DOC_DATE = "December 15, 2025"  # Update date
```

3. **Add New Section**:
```python
def add_section_17(doc, images):
    """Section 17: New Feature"""
    doc.add_heading("17. New Feature", level=1)
    doc.add_paragraph("Content here...")
    doc.add_page_break()

# Then add to sections list in main():
sections = [
    # ... existing sections ...
    ("Section 17: New Feature", add_section_17),
]
```

4. **Modify Colors**:
```python
PRIMARY_COLOR = RGBColor(0x3D, 0x7C, 0x72)  # Change RGB values
```

---

### Adding Images to Document

**Requirements**:
- Images must be in IMAGE_FOLDER
- Supported formats: .jpeg, .jpg, .png
- Name should be unique and descriptive

**Usage**:
```python
# Find specific image
my_images = [img for img in images if "keyword" in img]
if my_images:
    add_image_with_caption(doc, my_images[0], "Gambar X.Y - Caption")
```

---

### Creating Styled Tables

```python
add_styled_table(doc,
    ["Header 1", "Header 2", "Header 3"],  # Headers
    [
        ["Row 1 Col 1", "Row 1 Col 2", "Row 1 Col 3"],
        ["Row 2 Col 1", "Row 2 Col 2", "Row 2 Col 3"],
    ]  # Data rows
)
```

---

### Troubleshooting Script Issues

| Issue | Solution |
|-------|----------|
| `ModuleNotFoundError: docx` | Install: `pip install python-docx` |
| Path not found | Update IMAGE_FOLDER and OUTPUT_FILE to absolute paths |
| Images not appearing | Check IMAGE_FOLDER path and image file names |
| Formatting broken | Review OOXML element creation and styling |

---

## Common Tasks

### Task 1: Add New Feature Documentation

**Scenario**: Gateway app added a new "Logging Configuration" feature

**Steps**:
1. Read both markdown files to understand structure
2. Determine appropriate section number (e.g., Section 10)
3. Write content in Indonesian for `USER_GUIDE_CLEAN.md`:
   ```markdown
   ## 10. Logging Configurations

   Menu ini untuk mengatur penyimpanan log data...
   ```
4. Write content in English for `USER_GUIDE_MOBILE_APP.md`:
   ```markdown
   ## 10. Logging Configurations

   This menu configures data logging parameters...
   ```
5. Update table of contents in both files
6. Update section numbers of following sections
7. If generating Word doc, add `add_section_10()` function to Python script
8. Commit changes

---

### Task 2: Fix Technical Inaccuracy

**Scenario**: BLE timeout is actually 10 minutes, not 5 minutes

**Steps**:
1. Search for "5 menit" in `USER_GUIDE_CLEAN.md`
2. Replace with "10 menit" in all relevant locations
3. Search for "5 minutes" in `USER_GUIDE_MOBILE_APP.md`
4. Replace with "10 minutes"
5. Verify consistency in troubleshooting sections
6. Commit: `docs: fix BLE timeout duration (5→10 minutes)`

---

### Task 3: Update App Version References

**Scenario**: Mobile app updated from 1.0.0 to 1.0.1

**Steps**:
1. Update metadata tables in both markdown files:
   ```markdown
   | **Versi Aplikasi** | 1.0.1 |
   ```
2. Update `APP_VERSION` in Python script:
   ```python
   APP_VERSION = "1.0.1"
   ```
3. Update document version if needed (1.0 → 1.1)
4. Regenerate Word document
5. Commit: `docs: bump app version to 1.0.1`

---

### Task 4: Add Screenshot

**Scenario**: Adding new screenshot for a feature

**Steps**:
1. Save screenshot to IMAGE_FOLDER with timestamp name
2. Note the filename (e.g., `12.15.30.jpeg`)
3. Update Python script to include image:
   ```python
   new_feature_images = [img for img in images if "12.15.30" in img]
   if new_feature_images:
       add_image_with_caption(doc, new_feature_images[0],
                            "Gambar 7.3 - New Feature")
   ```
4. Regenerate document
5. Verify image appears correctly

---

### Task 5: Translate New Content

**Scenario**: English version has new section, needs Indonesian translation

**Steps**:
1. Read English content thoroughly
2. Identify technical terms to keep (MQTT, Modbus, etc.)
3. Translate to accessible Indonesian:
   - Use simple vocabulary
   - Avoid passive voice
   - Use imperative for instructions
4. Verify all parameter names match English version
5. Check examples are culturally appropriate
6. Commit both files together

---

## Related Repositories

### Gateway Firmware
- **Repository**: [GifariKemal/GatewaySuriotaPOC](https://github.com/GifariKemal/GatewaySuriotaPOC)
- **Technology**: ESP32, C/C++
- **Features**: Modbus RTU/TCP, MQTT, HTTP, BLE
- **Relevance**: Technical details for documentation accuracy

### Mobile Application
- **Repository**: [dickykhusnaedy/suriota_mobile_app](https://github.com/dickykhusnaedy/suriota_mobile_app)
- **Technology**: Flutter (Dart)
- **Platforms**: Android 5.0+, iOS 12+
- **Key Dependencies**:
  - `flutter_blue_plus` (BLE)
  - `get` (State management)
  - `go_router` (Navigation)
  - `file_picker` (File selection)
- **Relevance**: UI/UX details for screenshot accuracy

---

## Important Notes

### For AI Assistants Working on This Repository

1. **Primary Language**: Indonesian is the primary user-facing language
   - `USER_GUIDE_CLEAN.md` is the authoritative version
   - English version is more technical and detailed

2. **Always Maintain Consistency**:
   - Section numbers must align across both files
   - Technical parameters must match exactly
   - Version numbers must be synchronized

3. **When Adding Content**:
   - Write Indonesian first (user-friendly)
   - Write English second (technical)
   - Update Python script if generating Word docs
   - Update table of contents

4. **Images**:
   - Python script references Windows paths (may need update)
   - Images are optional but enhance clarity
   - Always add descriptive captions

5. **Technical Accuracy**:
   - Cross-reference with gateway firmware repo
   - Cross-reference with mobile app repo
   - Test procedures if possible
   - Verify parameter ranges and defaults

6. **Version Management**:
   - Document version tracks documentation changes
   - App version tracks mobile app releases
   - Both should be visible in metadata

7. **Commit Messages**:
   - Use conventional commits format
   - Prefix: `docs:` for all changes
   - Be specific about sections modified

8. **Before Committing**:
   - Check markdown syntax
   - Verify table formatting
   - Test links (if any)
   - Spell check (especially Indonesian)
   - Ensure consistent terminology

---

## Quick Reference

### File Paths

```bash
# Markdown files
/home/user/SRT-MGATE-1210-User-Guide/USER_GUIDE_CLEAN.md
/home/user/SRT-MGATE-1210-User-Guide/USER_GUIDE_MOBILE_APP.md

# Python script
/home/user/SRT-MGATE-1210-User-Guide/generate_user_guide_docx.py

# Generated Word document
/home/user/SRT-MGATE-1210-User-Guide/Panduan_Pengguna_Gateway_Config_App.docx
```

### Common Commands

```bash
# Generate Word document (if Python installed)
python generate_user_guide_docx.py

# View file structure
ls -la

# Search for term
grep -r "MQTT" *.md

# View git status
git status

# Commit changes
git add .
git commit -m "docs: description of changes"
git push
```

### Important Constants

```python
# From generate_user_guide_docx.py
DOC_VERSION = "1.0"
APP_VERSION = "1.0.0"
DOC_DATE = "30 November 2025"
PRIMARY_COLOR = RGBColor(0x3D, 0x7C, 0x72)  # SURIOTA teal
```

---

## Contact Information

**SURIOTA R&D Team**
- Email: support@suriota.com
- Website: www.suriota.com
- Documentation maintained by: Tim Dokumentasi SURIOTA

---

**End of CLAUDE.md** - This guide is designed to help AI assistants understand and maintain the SRT-MGATE-1210 user documentation repository effectively.
