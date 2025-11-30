# CLAUDE.md - AI Assistant Guide

**Repository**: SRT-MGATE-1210 User Guide Documentation
**Last Updated**: November 30, 2025
**Version**: 1.0

---

## Table of Contents

1. [Repository Overview](#repository-overview)
2. [Data Reference Sources](#data-reference-sources)
3. [Document Generation Pipeline](#document-generation-pipeline)
4. [Codebase Structure](#codebase-structure)
5. [File Descriptions](#file-descriptions)
6. [Development Workflows](#development-workflows)
7. [Key Conventions](#key-conventions)
8. [Documentation Standards](#documentation-standards)
9. [Python Script Guidelines](#python-script-guidelines)
10. [Pandoc Workflow](#pandoc-workflow)
11. [MCP Tools Integration](#mcp-tools-integration)
12. [Common Tasks](#common-tasks)
13. [Related Repositories](#related-repositories)
14. [Important Notes](#important-notes)

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

## Data Reference Sources

This documentation is compiled from **three primary data sources**. All information must be cross-referenced and validated against these sources to ensure accuracy.

### 1. Mobile Application Repository

**Repository**: [dickykhusnaedy/suriota_mobile_app](https://github.com/dickykhusnaedy/suriota_mobile_app)

**Technology Stack**:
- Flutter 3.x (Dart)
- Android SDK 34
- iOS 12+

**Reference Data**:

| Data Type | Usage in Documentation | Example |
|-----------|------------------------|---------|
| UI Screenshots | Visual step-by-step guides | Screen captures for BLE connection flow |
| Navigation Flow | Menu structure documentation | Home → Settings → Profile |
| Form Fields | Parameter tables | Device Name, Slave ID, Baudrate |
| BLE UUIDs | Technical specifications | Service UUID, Characteristic UUID |
| JSON Schemas | Configuration format examples | Device config structure |
| Error Messages | Troubleshooting section | "Connection timeout" errors |
| App Version | Document metadata | 1.0.0, 1.0.1, etc. |

**How to Fetch Data**:

```bash
# Clone repository
git clone https://github.com/dickykhusnaedy/suriota_mobile_app.git

# Key files to reference:
# - lib/screens/*.dart - UI screens and flows
# - lib/models/*.dart - Data models and JSON schemas
# - lib/services/ble_service.dart - BLE implementation
# - pubspec.yaml - App version and dependencies
```

**What to Extract**:
- Button labels and menu names
- Form validation rules
- Default values for parameters
- Navigation hierarchy
- Feature availability (which features are implemented)

---

### 2. Gateway Firmware Repository

**Repository**: [GifariKemal/GatewaySuriotaPOC](https://github.com/GifariKemal/GatewaySuriotaPOC)

**Technology Stack**:
- ESP32 (Espressif)
- Arduino/PlatformIO
- FreeRTOS

**Reference Data**:

| Data Type | Usage in Documentation | Example |
|-----------|------------------------|---------|
| Modbus Implementation | Function code support | FC 01, 03, 04, 16 |
| Data Types | Register configuration tables | INT16, FLOAT32_BE, UINT32_LE_BS |
| Default Values | Parameter recommendations | Default baudrate: 9600 |
| Valid Ranges | Input validation documentation | Slave ID: 1-247 |
| MQTT Topics | Server configuration examples | v1/devices/me/telemetry |
| Protocol Specs | Technical reference | MQTT keep-alive: 60s |
| BLE Services | Connection procedure details | Service UUID, timeout values |

**How to Fetch Data**:

```bash
# Clone repository
git clone https://github.com/GifariKemal/GatewaySuriotaPOC.git

# Key files to reference:
# - src/modbus_handler.cpp - Modbus implementation
# - src/mqtt_client.cpp - MQTT protocol
# - src/ble_provisioning.cpp - BLE service
# - include/config.h - Default values and constants
# - platformio.ini - Firmware version
```

**What to Extract**:
- Supported Modbus function codes
- Data type definitions and byte order
- Communication timeout values
- Buffer sizes and limits
- Firmware version compatibility
- BLE advertising interval and timeout

---

### 3. Product Datasheet

**File**: `6. Product_Suriota Modbus Gateway IIoT.pdf`

**Location**: `/home/user/SRT-MGATE-1210-User-Guide/6. Product_Suriota Modbus Gateway IIoT.pdf`

**Reference Data**:

| Data Type | Usage in Documentation | Section |
|-----------|------------------------|---------|
| Hardware Specifications | System requirements | Electrical ratings, dimensions |
| Modbus Support | Protocol capabilities | Function codes, data types |
| Communication Specs | Protocol reference | RS485 pinout, Ethernet specs |
| LED Indicators | Status monitoring guide | LED meanings and patterns |
| Certifications | Product information | CE, FCC compliance |
| Physical Dimensions | Installation guide | Mounting, clearance |

**How to Extract Data**:

```bash
# Extract text from PDF
pdftotext "6. Product_Suriota Modbus Gateway IIoT.pdf" datasheet.txt

# Or use Python
python -c "
from PyPDF2 import PdfReader
reader = PdfReader('6. Product_Suriota Modbus Gateway IIoT.pdf')
for page in reader.pages:
    print(page.extract_text())
"
```

**What to Extract**:
- Complete list of supported data types (30+ types)
- Electrical specifications (voltage, current, power)
- Environmental ratings (temperature, humidity)
- Physical dimensions and mounting options
- Communication port specifications
- Compliance and certification information

---

### 4. UI Assets Folder

**Location**: Referenced in `generate_user_guide_docx.py`

**Current Path** (Windows): `C:\Users\Administrator\Downloads\UI`

**Recommended Path** (Repository): `./assets/ui/` or `./images/screenshots/`

**Contents**:

| Asset Type | Format | Naming Convention | Usage |
|------------|--------|-------------------|-------|
| App Screenshots | JPEG/PNG | Timestamp (06.13.24.jpeg) | Step-by-step guides |
| Annotated Images | PNG | Feature name + timestamp | Highlighted features |
| Diagrams | SVG/PNG | descriptive-name.svg | Architecture diagrams |
| Icons | PNG | icon-name.png | Menu references |

**Screenshot Requirements**:
- **Resolution**: Minimum 1080x1920 (mobile), 1920x1080 (desktop)
- **Format**: PNG for UI (lossless), JPEG for photos
- **Annotations**: Use red boxes/arrows for callouts
- **Consistency**: Same device, same theme across all screenshots

**Organization**:
```
assets/ui/
├── mobile-app/
│   ├── 01-home-screen/
│   ├── 02-ble-scanning/
│   ├── 03-device-config/
│   └── ...
├── gateway-leds/
├── hardware/
└── diagrams/
```

---

### Data Synchronization Workflow

**When updating documentation**, follow this workflow to ensure consistency:

```
1. Check Mobile App Repo
   ↓
   Extract UI labels, validation rules
   ↓
2. Check Firmware Repo
   ↓
   Verify technical specifications
   ↓
3. Check Datasheet PDF
   ↓
   Confirm hardware specs
   ↓
4. Cross-Reference All Sources
   ↓
   Resolve conflicts (firmware takes precedence)
   ↓
5. Update Documentation
   ↓
   USER_GUIDE_CLEAN.md + USER_GUIDE_MOBILE_APP.md
   ↓
6. Generate Output
   ↓
   Pandoc → DOCX/PDF
```

**Conflict Resolution Priority**:
1. **Firmware repository** - Ground truth for technical implementation
2. **Mobile app repository** - UI/UX and user-facing labels
3. **Datasheet PDF** - Hardware specifications
4. **Existing documentation** - Lowest priority, update to match sources

---

## Document Generation Pipeline

### Overview

Documentation generation follows a **hybrid approach** using both Pandoc (primary) and Python-docx (supplementary):

```
Markdown Sources
      ↓
   [Pandoc]
      ↓
Basic DOCX/PDF ──→ [Python-docx] ──→ Enhanced DOCX
      ↓                                      ↓
   Distribution                        Final Output
```

### Why Hybrid Approach?

**Pandoc Strengths**:
- ✅ Fast conversion (seconds)
- ✅ Maintains markdown structure
- ✅ Excellent table handling
- ✅ Cross-references and links
- ✅ Professional typography
- ✅ Multi-format output (DOCX, PDF, HTML, EPUB)

**Pandoc Limitations**:
- ❌ Limited custom styling (brand colors)
- ❌ No custom cover page generation
- ❌ Basic image captions
- ❌ No info/warning boxes with colors
- ❌ Limited header/footer customization

**Python-docx Strengths**:
- ✅ Pixel-perfect custom styling
- ✅ SURIOTA brand colors (teal green)
- ✅ Professional cover page
- ✅ Advanced image captions
- ✅ Colored info/warning/tip boxes
- ✅ Custom headers/footers with page numbers

**Python-docx Limitations**:
- ❌ Slower processing (minutes for large docs)
- ❌ Manual section coding required
- ❌ Harder to maintain
- ❌ Word output only (no PDF directly)

### Recommended Pipeline

**Option A: Pandoc-First (Recommended for Speed)**

```bash
# Step 1: Convert with Pandoc
pandoc USER_GUIDE_CLEAN.md \
  --from=markdown+smart \
  --to=docx \
  --toc \
  --toc-depth=3 \
  --number-sections \
  --reference-doc=suriota-template.docx \
  -o draft.docx

# Step 2: Post-process with Python (optional)
python enhance_docx.py draft.docx final.docx
```

**Option B: Python-First (Recommended for Branding)**

```bash
# Generate with Python (includes branding)
python generate_user_guide_docx.py

# Convert to PDF
libreoffice --headless --convert-to pdf Panduan_Pengguna_Gateway_Config_App.docx
```

**Option C: Side-by-Side (Recommended for Both)**

```bash
# Generate both versions in parallel
pandoc USER_GUIDE_CLEAN.md -o Panduan_Gateway_Quick.docx &
python generate_user_guide_docx.py &
wait

# Use Pandoc version for quick updates
# Use Python version for official releases
```

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

## Pandoc Workflow

### Introduction to Pandoc

**Pandoc** is a universal document converter that excels at converting between markup formats. For this project, Pandoc is the **primary tool** for converting Markdown to Word (DOCX) and PDF formats.

### Installation

#### Linux (Debian/Ubuntu)
```bash
# Install pandoc
sudo apt update
sudo apt install pandoc

# Install LaTeX for PDF generation
sudo apt install texlive-latex-recommended texlive-fonts-recommended texlive-latex-extra

# Verify installation
pandoc --version
```

#### macOS
```bash
# Using Homebrew
brew install pandoc
brew install basictex

# Verify installation
pandoc --version
```

#### Windows
```powershell
# Using Chocolatey
choco install pandoc
choco install miktex

# Or download from https://pandoc.org/installing.html
```

---

### Basic Conversion Commands

#### Markdown to DOCX

**Simple Conversion**:
```bash
pandoc USER_GUIDE_CLEAN.md -o output.docx
```

**With Table of Contents**:
```bash
pandoc USER_GUIDE_CLEAN.md \
  --toc \
  --toc-depth=3 \
  -o Panduan_Gateway_Config_App.docx
```

**With Section Numbering**:
```bash
pandoc USER_GUIDE_CLEAN.md \
  --toc \
  --number-sections \
  -o Panduan_Gateway_Config_App.docx
```

**With Custom Reference Document (Styling)**:
```bash
# First, create a reference document
pandoc USER_GUIDE_CLEAN.md -o reference.docx

# Manually style reference.docx in Word (fonts, colors, headings)
# Save as suriota-template.docx

# Use template for future conversions
pandoc USER_GUIDE_CLEAN.md \
  --reference-doc=suriota-template.docx \
  --toc \
  --number-sections \
  -o Panduan_Gateway_Config_App.docx
```

---

#### Markdown to PDF

**Using XeLaTeX (Recommended)**:
```bash
pandoc USER_GUIDE_CLEAN.md \
  --pdf-engine=xelatex \
  --toc \
  --toc-depth=3 \
  --number-sections \
  -V geometry:margin=2.5cm \
  -V mainfont="Calibri" \
  -V fontsize=11pt \
  -o Panduan_Gateway_Config_App.pdf
```

**Using pdflatex**:
```bash
pandoc USER_GUIDE_CLEAN.md \
  --pdf-engine=pdflatex \
  --toc \
  -V geometry:margin=2.5cm \
  -o output.pdf
```

**With Custom LaTeX Template**:
```bash
# Get default template
pandoc -D latex > custom-template.tex

# Edit custom-template.tex to add branding
# ... add SURIOTA colors, logo, etc. ...

# Use custom template
pandoc USER_GUIDE_CLEAN.md \
  --template=custom-template.tex \
  --pdf-engine=xelatex \
  --toc \
  -o Panduan_Gateway_Config_App.pdf
```

---

### Advanced Pandoc Options

#### Metadata

Add document metadata using YAML frontmatter or command-line:

**YAML Frontmatter** (in markdown file):
```yaml
---
title: "Panduan Pengguna Gateway Config App"
author: "Tim Dokumentasi SURIOTA"
date: "30 November 2025"
version: "1.0"
subtitle: "SRT-MGATE-1210 Industrial IoT Gateway"
lang: id-ID
---
```

**Command-Line Metadata**:
```bash
pandoc USER_GUIDE_CLEAN.md \
  --metadata title="Panduan Pengguna Gateway Config App" \
  --metadata author="Tim Dokumentasi SURIOTA" \
  --metadata date="30 November 2025" \
  -o output.docx
```

---

#### Filters and Extensions

**Enable Smart Typography**:
```bash
pandoc USER_GUIDE_CLEAN.md \
  --from=markdown+smart \
  -o output.docx
```

Smart features include:
- `"quotes"` → "quotes" (curly quotes)
- `'quotes'` → 'quotes'
- `--` → – (en-dash)
- `---` → — (em-dash)
- `...` → … (ellipsis)

**Custom Filters**:
```bash
# Python filter example (filter.py)
pandoc USER_GUIDE_CLEAN.md \
  --filter=./filter.py \
  -o output.docx
```

---

#### Image Handling

**Resize Images**:
```markdown
![Caption](image.png){width=50%}
![Caption](image.png){width=300px}
```

**Center Images**:
```markdown
::: {style="text-align: center;"}
![Caption](image.png)
:::
```

**Add Image Captions**:
```bash
pandoc USER_GUIDE_CLEAN.md \
  --number-sections \
  --number-offset=0 \
  -o output.docx
```

---

### Creating Reference Template

To create a styled reference document with SURIOTA branding:

**Step 1: Generate Base Template**
```bash
pandoc USER_GUIDE_CLEAN.md -o suriota-base.docx
```

**Step 2: Style in Microsoft Word**

Open `suriota-base.docx` and modify:

1. **Styles → Modify**:
   - **Heading 1**: Font = Calibri Bold, Size = 18pt, Color = Teal (RGB 61, 124, 114)
   - **Heading 2**: Font = Calibri Bold, Size = 14pt, Color = Dark Teal (RGB 44, 92, 84)
   - **Heading 3**: Font = Calibri Bold, Size = 12pt, Color = Dark Gray
   - **Normal**: Font = Calibri, Size = 11pt, Line Spacing = 1.5

2. **Page Setup**:
   - Margins: 2.5cm all sides
   - Paper size: A4
   - Header/Footer: 1.25cm from edge

3. **Table Style**:
   - Create "SURIOTA Table" style
   - Header row: Teal background, white text
   - Alternating row colors

4. **Save As**: `suriota-template.docx`

**Step 3: Use Template**
```bash
pandoc USER_GUIDE_CLEAN.md \
  --reference-doc=suriota-template.docx \
  --toc \
  -o final_output.docx
```

---

### Automation Scripts

#### Bash Script: `build_docs.sh`

```bash
#!/bin/bash
# Build documentation in multiple formats

set -e

echo "Building documentation..."

# Variables
INPUT_MD="USER_GUIDE_CLEAN.md"
TEMPLATE="suriota-template.docx"
OUTPUT_DIR="output"

# Create output directory
mkdir -p "$OUTPUT_DIR"

# Build DOCX
echo "→ Building DOCX..."
pandoc "$INPUT_MD" \
  --from=markdown+smart \
  --to=docx \
  --reference-doc="$TEMPLATE" \
  --toc \
  --toc-depth=3 \
  --number-sections \
  --metadata title="Panduan Pengguna Gateway Config App" \
  --metadata author="Tim Dokumentasi SURIOTA" \
  --metadata date="$(date +'%d %B %Y')" \
  -o "$OUTPUT_DIR/Panduan_Gateway_Config_App.docx"

# Build PDF
echo "→ Building PDF..."
pandoc "$INPUT_MD" \
  --from=markdown+smart \
  --pdf-engine=xelatex \
  --toc \
  --toc-depth=3 \
  --number-sections \
  -V geometry:margin=2.5cm \
  -V mainfont="Calibri" \
  -V fontsize=11pt \
  --metadata title="Panduan Pengguna Gateway Config App" \
  --metadata author="Tim Dokumentasi SURIOTA" \
  -o "$OUTPUT_DIR/Panduan_Gateway_Config_App.pdf"

# Build HTML (bonus)
echo "→ Building HTML..."
pandoc "$INPUT_MD" \
  --from=markdown+smart \
  --to=html5 \
  --standalone \
  --toc \
  --css=style.css \
  -o "$OUTPUT_DIR/index.html"

echo "✓ Done! Output in $OUTPUT_DIR/"
```

**Usage**:
```bash
chmod +x build_docs.sh
./build_docs.sh
```

---

#### Python Script: `enhance_docx.py`

Post-process Pandoc output with Python-docx for advanced features:

```python
#!/usr/bin/env python3
"""
Enhance Pandoc-generated DOCX with SURIOTA branding
"""

from docx import Document
from docx.shared import RGBColor, Pt
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

def add_cover_page(doc):
    """Add SURIOTA branded cover page"""
    # Insert at beginning
    doc.add_page_break()
    # Move to end temporarily
    # Add content
    # ... (implementation from generate_user_guide_docx.py)

def add_page_numbers(doc):
    """Add page numbers to footer"""
    for section in doc.sections:
        footer = section.footer
        # Add page number field
        # ... (implementation)

def enhance_document(input_path, output_path):
    """Main enhancement function"""
    print(f"Loading {input_path}...")
    doc = Document(input_path)

    print("Adding cover page...")
    add_cover_page(doc)

    print("Adding page numbers...")
    add_page_numbers(doc)

    print(f"Saving to {output_path}...")
    doc.save(output_path)
    print("✓ Done!")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python enhance_docx.py input.docx output.docx")
        sys.exit(1)

    enhance_document(sys.argv[1], sys.argv[2])
```

**Usage**:
```bash
# Convert with Pandoc
pandoc USER_GUIDE_CLEAN.md -o draft.docx

# Enhance with Python
python enhance_docx.py draft.docx final.docx
```

---

### Pandoc Troubleshooting

| Issue | Solution |
|-------|----------|
| `pandoc: command not found` | Install pandoc: `sudo apt install pandoc` |
| LaTeX errors in PDF generation | Install full TeX distribution: `sudo apt install texlive-full` |
| Font not found | Use system fonts or install: `fc-list` to check available fonts |
| Images not appearing | Check image paths are relative to markdown file |
| Table formatting issues | Use grid tables instead of pipe tables |
| Reference doc not applied | Verify template path: `--reference-doc=./template.docx` |

---

## MCP Tools Integration

### Overview

**MCP (Model Context Protocol) Tools** enable AI assistants to fetch and analyze external documentation for comparative analysis and best practice extraction.

### Use Cases

1. **Competitive Analysis**: Compare user guide structure with industry leaders
2. **Best Practice Extraction**: Identify effective documentation patterns
3. **Quality Benchmarking**: Measure against professional standards
4. **Content Gap Analysis**: Find missing sections or topics

---

### Available MCP Tools

#### 1. WebFetch Tool

Fetch and analyze web pages, PDFs, and online documentation.

**Example: Fetch Competitor Manual**
```typescript
// Using MCP WebFetch
mcp.webfetch({
  url: "https://www.advantech.com/products/gateway-manual.pdf",
  prompt: "Extract table of contents structure and section organization"
})
```

**What to Analyze**:
- Table of contents depth and organization
- Section naming conventions
- Quick start guide placement
- Troubleshooting structure
- Visual aids usage (diagrams, screenshots)
- FAQ organization
- Appendix content

---

#### 2. WebSearch Tool

Search for best practices and examples.

**Example: Find Best User Guides**
```typescript
mcp.websearch({
  query: "industrial IoT gateway user manual PDF best practices 2024",
  max_results: 10
})
```

**Target Searches**:
- "Modbus gateway user manual PDF"
- "industrial IoT configuration guide"
- "mobile app setup guide examples"
- "technical documentation best practices"

---

### Comparative Analysis Framework

When analyzing competitor documentation:

#### Structure Comparison

| Aspect | Our Guide | Competitor A | Competitor B | Best Practice |
|--------|-----------|--------------|--------------|---------------|
| TOC Depth | 3 levels | 4 levels | 2 levels | 3-4 levels |
| Quick Start | Section 4 | Page 1 | Section 2 | First 3 pages |
| Screenshots | 15+ | 30+ | 5 | 20-30 ideal |
| Troubleshooting | Section 13 | Appendix | Section 8 | Before appendix |
| FAQ | Section 14 | Integrated | Dedicated | Both |
| Page Count | 35 pages | 60 pages | 20 pages | 30-50 pages |

#### Content Analysis

**Quick Start Guide**:
- ✅ Should be within first 5 pages
- ✅ Maximum 10 steps to basic operation
- ✅ Assumes zero prior knowledge
- ✅ Includes visual confirmation of success

**Troubleshooting**:
- ✅ Problem-solution table format
- ✅ Ordered by frequency (common issues first)
- ✅ Includes error codes/messages
- ✅ Cross-references to detailed sections

**Visual Aids**:
- ✅ Screenshot for every procedural step
- ✅ Annotated images (arrows, labels)
- ✅ Before/after comparisons
- ✅ Architecture diagrams

---

### Recommended Comparisons

#### Modbus Gateway Manufacturers

1. **Advantech**
   - Product: EKI-1221 Modbus Gateway
   - Manual URL: Check product page
   - Strengths: Detailed technical specs, troubleshooting

2. **Moxa**
   - Product: MGate Series
   - Strengths: Clear diagrams, configuration examples

3. **Phoenix Contact**
   - Product: FL MGUARD
   - Strengths: Professional layout, multi-language

#### Mobile Configuration Apps

1. **Ubiquiti UniFi**
   - Strengths: Visual setup wizard, screenshot-heavy

2. **TP-Link Deco**
   - Strengths: Simple language, step numbering

3. **Tasmota**
   - Strengths: Community-driven, comprehensive FAQ

---

### Extraction Checklist

When analyzing competitor docs, extract:

- [ ] **Structure**
  - [ ] TOC organization and depth
  - [ ] Section ordering logic
  - [ ] Quick start placement

- [ ] **Content**
  - [ ] Average section length (words/pages)
  - [ ] Technical detail level
  - [ ] Example-to-theory ratio

- [ ] **Visual Design**
  - [ ] Screenshot frequency
  - [ ] Diagram types used
  - [ ] Color scheme and branding
  - [ ] Typography hierarchy

- [ ] **User Experience**
  - [ ] Language complexity (Flesch score)
  - [ ] Assumed knowledge level
  - [ ] Procedural step count

- [ ] **Reference Materials**
  - [ ] Appendix organization
  - [ ] Index completeness
  - [ ] Glossary presence
  - [ ] Cross-referencing system

---

### Implementation

**Step 1: Research Phase**
```bash
# Use MCP tools to fetch 5-10 competitor manuals
mcp-fetch <url1> <url2> <url3>

# Extract and save analysis
```

**Step 2: Create Comparison Matrix**
```markdown
| Feature | Our Guide | Best-in-Class | Gap | Action |
|---------|-----------|---------------|-----|--------|
| Quick start | ❌ Section 4 | ✅ Page 1 | Position | Move earlier |
| Screenshots | ✅ 15+ | ✅ 30+ | Quantity | Add 10-15 more |
```

**Step 3: Implement Improvements**
```bash
# Update documentation based on findings
# Prioritize by impact and effort
```

**Step 4: Verify Quality**
```bash
# Check against best practices
# Measure readability scores
# Review with end users
```

---

### User Guide Quality Requirements

Based on industry best practices and competitive analysis, our user guides **MUST** meet these requirements:

#### ✅ Mandatory Elements

**Front Matter**:
- [ ] Professional cover page with logo
- [ ] Document metadata table (version, date, author)
- [ ] Table of contents (3 levels, page numbers)
- [ ] Document conventions/symbols explanation

**Content Organization**:
- [ ] Quick start guide (≤5 pages, first 10% of doc)
- [ ] Progressive complexity (basic → advanced)
- [ ] Logical section ordering (setup → operation → troubleshooting)
- [ ] Clear section numbering (1, 1.1, 1.1.1)

**Visual Aids**:
- [ ] Minimum 1 screenshot per procedural section
- [ ] Annotated images (arrows, labels, highlights)
- [ ] Architecture diagrams (system overview)
- [ ] Tables for all parameter reference

**Typography & Styling**:
- [ ] Consistent heading hierarchy (H1/H2/H3)
- [ ] Professional font (Calibri, Arial, or similar)
- [ ] Adequate white space (line spacing ≥1.15)
- [ ] Brand colors applied (SURIOTA teal)
- [ ] Page numbers on all pages (except cover)

**Content Quality**:
- [ ] Written for target audience (end users, not engineers)
- [ ] Active voice, imperative mood for instructions
- [ ] Realistic examples (not placeholder text)
- [ ] Consistent terminology throughout
- [ ] No jargon without explanation

**Reference Materials**:
- [ ] Comprehensive FAQ (10+ questions)
- [ ] Troubleshooting section (problem-solution format)
- [ ] Technical specifications appendix
- [ ] Contact information / support details

**Metadata & Credits**:
- [ ] Author attribution
- [ ] Copyright notice
- [ ] Version history/changelog
- [ ] Document series information (if applicable)

#### ✅ Quality Metrics

**Readability**:
- Flesch Reading Ease: 60-70 (standard)
- Average sentence length: ≤20 words
- Paragraph length: 3-5 sentences
- Procedure steps: ≤10 steps per task

**Completeness**:
- Coverage: 100% of app features
- Cross-reference accuracy: 100%
- Broken link count: 0
- Missing screenshot count: 0

**Usability**:
- Time to first success: ≤15 minutes
- User test success rate: ≥90%
- Support ticket reduction: ≥50%

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
