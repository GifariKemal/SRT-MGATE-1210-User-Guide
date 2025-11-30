# SRT-MGATE-1210 User Guide Documentation

[![Documentation](https://img.shields.io/badge/docs-latest-blue.svg)](https://github.com/GifariKemal/SRT-MGATE-1210-User-Guide)
[![Version](https://img.shields.io/badge/version-1.0-green.svg)]()
[![License](https://img.shields.io/badge/license-Proprietary-red.svg)]()

> **Comprehensive user documentation for SRT-MGATE-1210 Industrial IoT Gateway and Gateway Config App**

---

## 📋 Table of Contents

- [Overview](#overview)
- [Documentation Files](#documentation-files)
- [Reference Sources](#reference-sources)
- [Getting Started](#getting-started)
- [Building Documentation](#building-documentation)
- [Documentation Standards](#documentation-standards)
- [Contributing](#contributing)
- [Related Projects](#related-projects)
- [Support](#support)

---

## 🎯 Overview

This repository contains end-user documentation for the **SRT-MGATE-1210 Industrial IoT Gateway** system, including:

- **Gateway Hardware**: Industrial-grade Modbus RTU/TCP gateway with WiFi/Ethernet connectivity
- **Mobile Application**: Flutter-based configuration app for Android and iOS
- **Cloud Integration**: MQTT and HTTP protocols for real-time data transmission

### Target Audience

- **End Users**: Field technicians, operators, and installers
- **System Integrators**: Engineers implementing IoT solutions
- **Developers**: Software developers integrating with the gateway system

### Languages

- 🇮🇩 **Indonesian (Bahasa Indonesia)**: Primary user-facing documentation
- 🇬🇧 **English**: Technical reference and developer documentation

---

## 📚 Documentation Files

### Markdown Source Files

| File | Language | Purpose | Target Audience |
|------|----------|---------|-----------------|
| `USER_GUIDE_CLEAN.md` | 🇮🇩 Indonesian | User-friendly setup and operation guide | End users, technicians |
| `USER_GUIDE_MOBILE_APP.md` | 🇬🇧 English | Technical reference with API details | Developers, integrators |

### Generated Documents

| File | Format | Generated From | Purpose |
|------|--------|----------------|---------|
| `Panduan_Pengguna_Gateway_Config_App.docx` | Word | Python script | Professional print-ready document |
| *(Future)* PDF output | PDF | Pandoc conversion | Digital distribution |

### Scripts & Tools

| File | Type | Purpose |
|------|------|---------|
| `generate_user_guide_docx.py` | Python | Legacy Word document generator |
| *(Planned)* `convert_with_pandoc.sh` | Bash | Pandoc-based conversion pipeline |

### Reference Materials

| File | Type | Source |
|------|------|--------|
| `6. Product_Suriota Modbus Gateway IIoT.pdf` | PDF | Official datasheet |
| *(External)* UI Screenshots | Images | Mobile app repository |
| *(External)* Firmware specs | Code | Gateway firmware repository |

---

## 🔗 Reference Sources

This documentation is compiled from **three primary sources**:

### 1. 📱 Mobile Application Repository
- **Repository**: [dickykhusnaedy/suriota_mobile_app](https://github.com/dickykhusnaedy/suriota_mobile_app)
- **Technology**: Flutter (Dart)
- **Reference Data**:
  - UI/UX screenshots for user guide illustrations
  - App version numbers and feature descriptions
  - BLE service UUIDs and characteristics
  - Configuration parameter formats (JSON schemas)
  - Navigation flow and menu structure

### 2. 🔧 Gateway Firmware Repository
- **Repository**: [GifariKemal/GatewaySuriotaPOC](https://github.com/GifariKemal/GatewaySuriotaPOC)
- **Technology**: ESP32 (C/C++)
- **Reference Data**:
  - Modbus RTU/TCP implementation details
  - MQTT/HTTP protocol specifications
  - WiFi/Ethernet configuration parameters
  - BLE advertising and service structure
  - Default values and valid ranges
  - Firmware version compatibility matrix

### 3. 📄 Product Datasheet
- **File**: `6. Product_Suriota Modbus Gateway IIoT.pdf`
- **Reference Data**:
  - Hardware specifications
  - Electrical ratings and pinouts
  - Supported Modbus function codes
  - Data type specifications (30+ types)
  - Communication protocols and standards
  - Physical dimensions and mounting

### 4. 🖼️ UI Assets
- **Location**: UI screenshots folder (referenced in Python script)
- **Content**:
  - Mobile app screen captures
  - Step-by-step visual guides
  - Configuration examples
  - Status indicators and icons

---

## 🚀 Getting Started

### Prerequisites

**For Reading Documentation:**
- Markdown viewer (VS Code, Typora, etc.)
- PDF reader
- Word processor (for .docx files)

**For Building Documentation:**
```bash
# Install pandoc (primary conversion tool)
sudo apt install pandoc texlive-latex-recommended texlive-fonts-recommended

# Install Python dependencies (for additional processing)
pip install python-docx pypandoc

# Optional: Install MCP tools for web scraping
# (See MCP Tools section)
```

### Quick Start

1. **Clone this repository**:
   ```bash
   git clone https://github.com/GifariKemal/SRT-MGATE-1210-User-Guide.git
   cd SRT-MGATE-1210-User-Guide
   ```

2. **View documentation**:
   - Indonesian guide: Open `USER_GUIDE_CLEAN.md`
   - English guide: Open `USER_GUIDE_MOBILE_APP.md`
   - Datasheet: Open `6. Product_Suriota Modbus Gateway IIoT.pdf`

3. **Build Word/PDF output** (see [Building Documentation](#building-documentation))

---

## 🔨 Building Documentation

### Method 1: Pandoc Conversion (Recommended)

Pandoc is the primary tool for converting Markdown to Word/PDF with advanced formatting.

#### Convert to DOCX (Word)

```bash
# Basic conversion
pandoc USER_GUIDE_CLEAN.md -o output.docx

# With custom reference document for styling
pandoc USER_GUIDE_CLEAN.md \
  --reference-doc=template.docx \
  -o Panduan_Gateway_Config_App.docx

# With table of contents
pandoc USER_GUIDE_CLEAN.md \
  --toc \
  --toc-depth=3 \
  --reference-doc=template.docx \
  -o Panduan_Gateway_Config_App.docx
```

#### Convert to PDF

```bash
# Using LaTeX engine
pandoc USER_GUIDE_CLEAN.md \
  --pdf-engine=xelatex \
  --toc \
  -V geometry:margin=2.5cm \
  -V mainfont="Calibri" \
  -o Panduan_Gateway_Config_App.pdf

# With custom template
pandoc USER_GUIDE_CLEAN.md \
  --template=custom-template.tex \
  --pdf-engine=xelatex \
  --toc \
  -o output.pdf
```

#### Advanced Pandoc Options

```bash
# Full-featured conversion with metadata
pandoc USER_GUIDE_CLEAN.md \
  --from=markdown+smart \
  --to=docx \
  --toc \
  --toc-depth=3 \
  --number-sections \
  --reference-doc=suriota-template.docx \
  --metadata title="Panduan Pengguna Gateway Config App" \
  --metadata author="Tim Dokumentasi SURIOTA" \
  --metadata date="30 November 2025" \
  -o Panduan_Gateway_Config_App.docx
```

### Method 2: Python Script (Legacy/Supplementary)

For features not supported by Pandoc (custom styling, image captions, etc.):

```bash
# Generate Word document with Python
python generate_user_guide_docx.py
```

**Note**: The Python script includes:
- Custom SURIOTA brand colors
- Professional cover page
- Image insertion with captions
- Styled info/warning boxes
- Page numbering and headers/footers

### Method 3: Hybrid Approach (Best Results)

1. **Initial conversion with Pandoc**:
   ```bash
   pandoc USER_GUIDE_CLEAN.md \
     --toc \
     --reference-doc=template.docx \
     -o draft.docx
   ```

2. **Post-process with Python** (for advanced features):
   ```python
   from docx import Document

   # Load pandoc output
   doc = Document('draft.docx')

   # Add custom elements
   # - Brand colors
   # - Cover page
   # - Image captions
   # - Note boxes

   doc.save('final_output.docx')
   ```

---

## 📐 Documentation Standards

### Structure Requirements

All user guides **MUST** include:

✅ **Cover Page**
- Document title and subtitle
- Version information (document and app)
- Publication date
- Author/organization
- Brand logo

✅ **Table of Contents**
- Auto-generated with page numbers
- 3-level hierarchy minimum
- Hyperlinked sections (digital versions)

✅ **Page Numbers**
- Footer placement
- Format: "Page X of Y" or "Halaman X"
- Excluded from cover page

✅ **Headers/Footers**
- Document title in header
- Copyright notice in footer
- Consistent across all pages

✅ **Document Credits/Metadata**
- Author attribution
- Version history
- Document series information
- Copyright notice
- Contact information

### Content Integration

User guides must seamlessly integrate information from:

1. **Firmware Documentation** → Technical specifications
   - Default baudrate, timeout values
   - Supported Modbus function codes
   - MQTT broker compatibility
   - Register address ranges

2. **Mobile App Documentation** → User interface guidance
   - Screen navigation flows
   - Button labels and icons
   - Form field requirements
   - Error messages and troubleshooting

3. **Product Datasheet** → Hardware specifications
   - Electrical ratings
   - Physical dimensions
   - Communication ports
   - LED indicator meanings

4. **UI Screenshots** → Visual step-by-step guides
   - Annotated screenshots
   - Numbered steps matching images
   - Before/after comparisons
   - Error state examples

### Formatting Standards

#### Typography

```markdown
# Headers: Progressive hierarchy
H1: Main sections (e.g., "1. Introduction")
H2: Subsections (e.g., "1.1 About This Guide")
H3: Sub-subsections (e.g., "1.1.1 Target Audience")

# Text formatting
**Bold**: Important terms, field names, button labels
*Italic*: Filenames, technical terms, emphasis
`Code`: Parameter values, commands, JSON keys
```

#### Tables

All parameter tables must include:
- **Parameter name**
- **Description**
- **Example value**
- **Valid range** (if applicable)
- **Default value** (if applicable)

Example:
```markdown
| Parameter | Description | Example | Range | Default |
|-----------|-------------|---------|-------|---------|
| Baudrate | Serial speed | 9600 | 1200-115200 | 9600 |
| Slave ID | Device address | 1 | 1-247 | 1 |
```

#### Code Blocks

Use language-specific syntax highlighting:

```json
{
  "device_id": "SRT-MGATE-001",
  "data": {
    "temperature": 25.5
  }
}
```

```bash
mosquitto_sub -h broker.hivemq.com -t "device/data"
```

#### Lists

- **Numbered lists**: For sequential steps, procedures
- **Bullet lists**: For features, specifications, non-sequential items
- **Checklist**: For pre-flight checks, requirements

#### Note Boxes

Use consistent formatting for callouts:

> **💡 Tip**: Best practice recommendations
>
> **⚠️ Warning**: Actions that may cause data loss or damage
>
> **ℹ️ Note**: Additional information or context

---

## 🤖 MCP Tools Integration

### Scraping Competitor Documentation

Use MCP tools to analyze similar user guides and manual books:

#### 1. Web Fetch Tool

```bash
# Fetch user manuals from competitor websites
mcp-fetch https://example.com/gateway-manual.pdf
mcp-fetch https://competitor.com/user-guide
```

#### 2. Document Analysis

Compare structure and content:
- Table of contents depth
- Section organization
- Visual aids usage
- Language clarity
- Technical detail level

#### 3. Best Practices Extraction

Identify patterns in top-rated manuals:
- Quick start guide placement
- Troubleshooting section structure
- FAQ organization
- Appendix content
- Index completeness

### Recommended Comparisons

Analyze user guides from:
- **Modbus Gateways**: Advantech, Moxa, Phoenix Contact
- **IoT Gateways**: Siemens, Schneider Electric, ABB
- **Mobile Config Apps**: Ubiquiti, TP-Link, Tasmota

---

## 🏗️ Architecture & Design

### Document Architecture

```
User Guide
├── Front Matter
│   ├── Cover Page
│   ├── Table of Contents
│   ├── Document Information
│   └── Version History
│
├── Introduction
│   ├── About the Product
│   ├── About This Guide
│   ├── Target Audience
│   └── Document Conventions
│
├── Getting Started
│   ├── System Requirements
│   ├── Installation (App)
│   ├── First-Time Setup
│   └── Quick Start Guide
│
├── Configuration
│   ├── BLE Connection
│   ├── Network Setup (WiFi/Ethernet)
│   ├── Device Communications (Modbus)
│   ├── Data Register Mapping
│   └── Server Configuration (MQTT/HTTP)
│
├── Operation
│   ├── Monitoring Data
│   ├── Backup/Restore
│   ├── Firmware Updates
│   └── Best Practices
│
├── Troubleshooting
│   ├── Common Issues
│   ├── Error Messages
│   ├── FAQ
│   └── Support Contacts
│
└── Appendices
    ├── Technical Specifications
    ├── Data Type Reference
    ├── MQTT Payload Examples
    ├── Modbus Function Codes
    └── Glossary
```

### Information Flow

```
Datasheet (PDF)
      ↓
   [Extract]
      ↓
Technical Specs ──┐
                  │
Firmware Repo     ├──→ USER_GUIDE_MOBILE_APP.md ──┐
      ↓           │         (English)              │
   [Analyze]      │                                │
      ↓           │                                ├──→ DOCX/PDF
Implementation ───┤                                │         ↓
Details           │                                │    Distribution
                  │                                │
Mobile App Repo   ├──→ USER_GUIDE_CLEAN.md ───────┘
      ↓           │         (Indonesian)
   [Document]     │
      ↓           │
UI/UX Flow ───────┘

Legend:
[Extract]  = Data extraction process
[Analyze]  = Code analysis and documentation
[Document] = Screenshot and flow documentation
```

---

## 🤝 Contributing

### Updating Documentation

1. **For content updates**:
   - Edit `USER_GUIDE_CLEAN.md` (Indonesian)
   - Edit `USER_GUIDE_MOBILE_APP.md` (English)
   - Ensure consistency across both files

2. **For new features**:
   - Add section to both markdown files
   - Update table of contents
   - Add screenshots to UI folder
   - Update Python script (if using)

3. **Version bumping**:
   - Update metadata in markdown files
   - Update `DOC_VERSION` in Python script
   - Update CHANGELOG (if exists)

### Git Workflow

```bash
# Create feature branch
git checkout -b docs/add-new-feature

# Make changes
# ... edit files ...

# Commit with conventional commits
git add .
git commit -m "docs: add section for logging configuration"

# Push to remote
git push origin docs/add-new-feature

# Create pull request
```

### Commit Message Format

Follow [Conventional Commits](https://www.conventionalcommits.org/):

```
docs: update BLE timeout from 5 to 10 minutes
docs: add troubleshooting section for WiFi issues
docs: fix typo in Modbus register table
docs: bump version to 1.1
```

---

## 🔗 Related Projects

### Gateway Firmware
- **Repository**: [GifariKemal/GatewaySuriotaPOC](https://github.com/GifariKemal/GatewaySuriotaPOC)
- **Technology**: ESP32, Arduino, PlatformIO
- **Features**:
  - Modbus RTU/TCP master
  - MQTT client with TLS
  - HTTP POST client
  - BLE provisioning
  - WiFi/Ethernet dual-stack

### Mobile Application
- **Repository**: [dickykhusnaedy/suriota_mobile_app](https://github.com/dickykhusnaedy/suriota_mobile_app)
- **Technology**: Flutter 3.x (Dart)
- **Platforms**: Android 5.0+, iOS 12+
- **Key Dependencies**:
  - `flutter_blue_plus` - BLE communication
  - `get` - State management
  - `go_router` - Navigation
  - `file_picker` - Config import/export

---

## 📞 Support

### Documentation Team
- **Email**: support@suriota.com
- **Website**: [www.suriota.com](https://www.suriota.com)
- **Hours**: Monday - Friday, 08:00 - 17:00 WIB (UTC+7)

### Report Issues
- **GitHub Issues**: [SRT-MGATE-1210-User-Guide/issues](https://github.com/GifariKemal/SRT-MGATE-1210-User-Guide/issues)
- **Categories**:
  - 📝 Documentation errors or typos
  - 🔧 Technical inaccuracies
  - 💡 Improvement suggestions
  - 🌐 Translation issues

### Contributing
See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines on:
- Documentation style guide
- Markdown formatting
- Screenshot requirements
- Translation workflow
- Review process

---

## 📄 License

**Copyright © 2025 PT SURIOTA Technology Indonesia**

This documentation is proprietary and confidential. Unauthorized reproduction or distribution is prohibited.

For licensing inquiries, contact: support@suriota.com

---

## 🏆 Credits

### Authors
- **Tim Dokumentasi SURIOTA** - Initial documentation
- **AI Assistants** - Documentation maintenance and updates

### Contributors
See [CONTRIBUTORS.md](CONTRIBUTORS.md) for a complete list of contributors.

### Tools & Technologies
- [Pandoc](https://pandoc.org/) - Universal document converter
- [Python-docx](https://python-docx.readthedocs.io/) - Python Word processing
- [Markdown](https://www.markdownguide.org/) - Lightweight markup language
- [Flutter](https://flutter.dev/) - Mobile app framework
- [ESP32](https://www.espressif.com/en/products/socs/esp32) - Gateway hardware platform

---

## 📊 Document Status

| Document | Version | Last Updated | Status |
|----------|---------|--------------|--------|
| USER_GUIDE_CLEAN.md | 1.0 | 2025-11-30 | ✅ Current |
| USER_GUIDE_MOBILE_APP.md | 2.1 | 2025-11-30 | ✅ Current |
| Datasheet PDF | 1.0 | 2025-11-30 | 📥 Pending upload |
| DOCX Output | 1.0 | 2025-11-30 | ✅ Generated |

---

## 🗺️ Roadmap

- [ ] Upload product datasheet PDF
- [ ] Create pandoc conversion scripts
- [ ] Add UI screenshots folder
- [ ] Generate PDF version
- [ ] Create video tutorials
- [ ] Add multilingual support (additional languages)
- [ ] Interactive web documentation
- [ ] API documentation integration

---

**Last Updated**: November 30, 2025
**Maintained by**: SURIOTA Documentation Team
**Document Version**: 1.0
