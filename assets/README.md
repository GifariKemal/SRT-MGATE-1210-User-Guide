# Assets Folder

This folder contains all visual and template assets for documentation generation.

## Folder Structure

```
assets/
├── ui/                      # User interface screenshots and images
│   ├── mobile-app/         # Mobile application screenshots
│   ├── gateway-hardware/   # Gateway device photos and LED indicators
│   └── diagrams/           # Architecture and flow diagrams
└── templates/              # Document templates
    └── suriota-template.docx  # SURIOTA branded Word template
```

## UI Screenshots

### Mobile App Screenshots

**Location**: `ui/mobile-app/`

**Naming Convention**: Use descriptive names with timestamps
- Format: `{feature}-{timestamp}.png` or `{section}-{step}-{timestamp}.jpg`
- Examples:
  - `home-screen-06.13.24.png`
  - `ble-scanning-06.13.23.png`
  - `device-config-form-06.13.22.png`

**Requirements**:
- **Resolution**: Minimum 1080x1920 (portrait), 1920x1080 (landscape)
- **Format**: PNG (preferred for UI), JPEG (acceptable for photos)
- **Quality**: High resolution, clear text, no blur
- **Consistency**: Same device model, same theme (light/dark)
- **Annotations**: Use red arrows/boxes for highlights (optional)

**Recommended Screenshots**:
1. Home screen (empty state)
2. Home screen (with devices)
3. Scan devices screen
4. Scanning in progress
5. Scan results
6. Connection confirmation dialog
7. Device detail/dashboard
8. Device communications list
9. Add device form (RTU)
10. Add device form (TCP)
11. Modbus configurations list
12. Add register form
13. Server configurations (WiFi/Ethernet)
14. Server configurations (MQTT)
15. Server configurations (Topic setup)
16. Device status screen
17. Settings menu
18. Backup/restore dialogs
19. App settings
20. Error states and dialogs

### Gateway Hardware Photos

**Location**: `ui/gateway-hardware/`

**Content**:
- Gateway device front view
- Gateway device back view (ports and labels)
- LED indicators (different states)
- Connection ports close-up
- Mounting options
- DIN rail installation

### Diagrams

**Location**: `ui/diagrams/`

**Content**:
- System architecture diagram
- BLE connection flow
- Data flow (sensor → gateway → cloud)
- Network topology
- MQTT topic structure
- Configuration workflow

**Format**: SVG (preferred) or high-resolution PNG

**Tools**: Draw.io, Lucidchart, Figma, or similar

## Templates

### SURIOTA Word Template

**Location**: `templates/suriota-template.docx`

**Purpose**: Reference document for Pandoc styling

**Creation Steps**:
1. Generate base document with Pandoc
2. Open in Microsoft Word
3. Modify styles:
   - Heading 1: Calibri Bold 18pt, Teal (RGB 61,124,114)
   - Heading 2: Calibri Bold 14pt, Dark Teal (RGB 44,92,84)
   - Heading 3: Calibri Bold 12pt, Dark Gray
   - Normal: Calibri 11pt, Line spacing 1.5
4. Set page margins (2.5cm all sides)
5. Create table style (teal header)
6. Save as template

**Usage**:
```bash
pandoc USER_GUIDE_CLEAN.md \
  --reference-doc=assets/templates/suriota-template.docx \
  -o output.docx
```

## Adding New Assets

### Screenshots

1. Take screenshot with required resolution
2. Crop if needed (remove status bar for mobile)
3. Name descriptively with timestamp
4. Save to appropriate subfolder
5. Reference in markdown:
   ```markdown
   ![Screenshot description](assets/ui/mobile-app/screenshot-name.png)
   ```

### Diagrams

1. Create diagram in vector tool
2. Export as SVG (preferred) or PNG (300 DPI)
3. Name descriptively (no timestamps)
4. Save to `diagrams/` folder
5. Reference in markdown:
   ```markdown
   ![Architecture Diagram](assets/ui/diagrams/system-architecture.svg)
   ```

## Image Optimization

Before adding images to repository:

```bash
# Optimize PNG (lossless)
optipng -o7 screenshot.png

# Optimize JPEG (quality 85)
jpegoptim --max=85 photo.jpg

# Convert to WebP (modern format, smaller size)
cwebp -q 80 image.png -o image.webp
```

## Gitignore Recommendations

Add to `.gitignore` if using temporary files:
```
assets/ui/temp/
assets/ui/*.tmp
assets/ui/*.bak
```

## Copyright Notice

All screenshots and images are property of PT SURIOTA Technology Indonesia.
Unauthorized use is prohibited.

---

**Last Updated**: November 30, 2025
**Maintained by**: SURIOTA Documentation Team
