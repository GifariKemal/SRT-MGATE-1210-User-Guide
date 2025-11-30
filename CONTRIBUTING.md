# Contributing to SRT-MGATE-1210 User Guide

Thank you for considering contributing to the SRT-MGATE-1210 User Guide documentation!

This document provides guidelines for contributing to this project.

---

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Workflow](#development-workflow)
- [Documentation Standards](#documentation-standards)
- [Commit Guidelines](#commit-guidelines)
- [Pull Request Process](#pull-request-process)
- [Review Criteria](#review-criteria)

---

## Code of Conduct

### Our Pledge

We are committed to providing a welcoming and inspiring environment for all contributors.

### Expected Behavior

- Use welcoming and inclusive language
- Be respectful of differing viewpoints
- Accept constructive criticism gracefully
- Focus on what is best for the community
- Show empathy towards other contributors

### Unacceptable Behavior

- Trolling, insulting comments, or personal attacks
- Public or private harassment
- Publishing others' private information
- Other conduct which could be considered inappropriate

---

## Getting Started

### Prerequisites

**Software Requirements**:
```bash
# Required
- Git
- Markdown editor (VS Code, Typora, etc.)
- Pandoc (for document generation)
- Python 3.x (for Python scripts)

# Optional
- python-docx (for enhanced document generation)
- LaTeX (for PDF generation)
```

**Knowledge Requirements**:
- Basic Markdown syntax
- Git workflow (clone, commit, push, pull request)
- Indonesian language (for USER_GUIDE_CLEAN.md)
- English language (for USER_GUIDE_MOBILE_APP.md)

### Setup Development Environment

1. **Clone the repository**:
   ```bash
   git clone https://github.com/GifariKemal/SRT-MGATE-1210-User-Guide.git
   cd SRT-MGATE-1210-User-Guide
   ```

2. **Install dependencies**:
   ```bash
   # Install Pandoc (Ubuntu/Debian)
   sudo apt install pandoc

   # Install Python dependencies
   pip install python-docx

   # Install LaTeX (optional, for PDF)
   sudo apt install texlive-latex-recommended texlive-fonts-recommended
   ```

3. **Verify installation**:
   ```bash
   pandoc --version
   python --version
   ```

4. **Read documentation**:
   - `README.md` - Project overview
   - `CLAUDE.md` - AI assistant guide (comprehensive reference)
   - This file (`CONTRIBUTING.md`)

---

## Development Workflow

### Branching Strategy

We use a feature branch workflow:

```
main (protected)
  ↓
  ├─ docs/feature-name-1
  ├─ docs/feature-name-2
  └─ docs/bugfix-name
```

**Branch Naming**:
- Features: `docs/feature-description`
- Bug fixes: `docs/fix-description`
- Updates: `docs/update-description`

### Typical Workflow

1. **Create a feature branch**:
   ```bash
   git checkout -b docs/add-logging-section
   ```

2. **Make changes**:
   - Edit `USER_GUIDE_CLEAN.md` (Indonesian)
   - Edit `USER_GUIDE_MOBILE_APP.md` (English)
   - Keep both files synchronized

3. **Test your changes**:
   ```bash
   # Generate documentation
   ./scripts/build_docs.sh

   # Check output
   ls output/
   ```

4. **Commit changes**:
   ```bash
   git add USER_GUIDE_CLEAN.md USER_GUIDE_MOBILE_APP.md
   git commit -m "docs: add logging configuration section"
   ```

5. **Push to remote**:
   ```bash
   git push origin docs/add-logging-section
   ```

6. **Create Pull Request** on GitHub

---

## Documentation Standards

### Language Guidelines

#### Indonesian (USER_GUIDE_CLEAN.md)

**Tone**: Friendly, accessible, non-technical

**Writing Style**:
- Use **imperative mood** for instructions ("Tekan", "Pilih", "Isi")
- Keep sentences short (≤20 words)
- Avoid technical jargon
- Use active voice
- Provide clear examples

**Example**:
```markdown
✓ Tekan tombol Scan untuk memulai pencarian perangkat
✗ Proses scanning perangkat dapat dimulai dengan menekan tombol Scan
```

#### English (USER_GUIDE_MOBILE_APP.md)

**Tone**: Technical, precise, professional

**Writing Style**:
- Use technical terminology where appropriate
- Include code examples and JSON payloads
- Reference source code when relevant
- Provide detailed specifications

**Example**:
```markdown
✓ Subscribe to the MQTT topic using mosquitto_sub:
   mosquitto_sub -h broker.hivemq.com -p 1883 -t "topic"

✗ Dengarkan data dari broker menggunakan program khusus
```

### Formatting Standards

#### Headings

```markdown
# Level 1: Main sections (1. Introduction)
## Level 2: Subsections (1.1 About This Guide)
### Level 3: Sub-subsections (procedural steps)
```

#### Lists

```markdown
# Numbered lists for sequential steps
1. First step
2. Second step
3. Third step

# Bullet lists for features/items
- Feature one
- Feature two
- Feature three
```

#### Tables

```markdown
| Parameter | Description | Example |
|-----------|-------------|---------|
| Device Name | Device identifier | "Sensor_01" |
| Slave ID | Modbus address (1-247) | 1 |
```

#### Code Blocks

````markdown
```json
{
  "device_id": "SRT-MGATE-001",
  "data": {...}
}
```

```bash
mosquitto_sub -h broker.hivemq.com -t "topic"
```
````

#### Note Boxes

```markdown
> **💡 Tip**: Use this for helpful suggestions
>
> **⚠️ Warning**: Use this for important warnings
>
> **ℹ️ Note**: Use this for additional information
```

---

## Commit Guidelines

### Commit Message Format

We follow [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>: <description>

[optional body]

[optional footer]
```

**Types**:
- `docs:` - Documentation changes
- `feat:` - New features
- `fix:` - Bug fixes
- `style:` - Formatting changes
- `refactor:` - Code refactoring
- `chore:` - Maintenance tasks

### Examples

**Good Commit Messages**:
```
docs: add BLE connection troubleshooting section

- Add common BLE issues to section 13
- Include solutions for connection timeout
- Update FAQ with BLE questions
```

```
docs: fix typo in Modbus data types table

Corrected FLOAT32_BE description in section 8.6
```

```
docs: update app version to 1.0.1

- Update metadata in both markdown files
- Update Python script DOC_VERSION
- Regenerate Word document
```

**Bad Commit Messages**:
```
✗ update docs
✗ fixed stuff
✗ changes
```

---

## Pull Request Process

### Before Submitting

**Checklist**:
- [ ] Both Indonesian and English files updated (if applicable)
- [ ] Table of contents updated
- [ ] Section numbers consistent across both files
- [ ] Markdown syntax validated
- [ ] No typos or grammar errors
- [ ] Examples are realistic and accurate
- [ ] Technical details verified against source repositories
- [ ] Documentation builds without errors

### PR Title Format

Follow the same format as commit messages:

```
docs: add logging configuration section
```

### PR Description Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] New section
- [ ] Update existing content
- [ ] Fix error/typo
- [ ] Improve clarity
- [ ] Add screenshots

## Related Issues
Closes #123

## Checklist
- [ ] Indonesian file updated
- [ ] English file updated
- [ ] Table of contents updated
- [ ] Tested document generation
- [ ] No markdown errors

## Screenshots (if applicable)
[Add screenshots of generated output]

## Additional Notes
Any additional context
```

### Review Process

1. **Automated Checks** (if configured):
   - Markdown linting
   - Link validation
   - Spell check

2. **Manual Review**:
   - Technical accuracy
   - Language quality
   - Formatting consistency
   - Cross-reference validity

3. **Approval Requirements**:
   - At least 1 approving review
   - All discussions resolved
   - CI checks passing (if applicable)

4. **Merge**:
   - Squash and merge (default)
   - Rebase and merge (for clean history)

---

## Review Criteria

### Technical Accuracy

Reviewers will verify:
- [ ] Information matches firmware repository
- [ ] UI labels match mobile app repository
- [ ] Hardware specs match datasheet
- [ ] Default values are correct
- [ ] Valid ranges are accurate

### Language Quality

Reviewers will check:
- [ ] Grammar and spelling
- [ ] Sentence clarity
- [ ] Appropriate tone for audience
- [ ] Consistent terminology
- [ ] Translation accuracy (ID ↔ EN)

### Formatting

Reviewers will ensure:
- [ ] Consistent heading levels
- [ ] Proper table formatting
- [ ] Code blocks with syntax highlighting
- [ ] Image references are valid
- [ ] Cross-references work

### Completeness

Reviewers will confirm:
- [ ] All steps documented
- [ ] Examples provided
- [ ] Edge cases covered
- [ ] Troubleshooting included
- [ ] FAQ updated (if needed)

---

## File Structure

### What to Edit

**Documentation**:
- `USER_GUIDE_CLEAN.md` - Indonesian user guide
- `USER_GUIDE_MOBILE_APP.md` - English technical guide
- `README.md` - Project readme
- `CLAUDE.md` - AI assistant guide
- `assets/ui/` - Screenshots and images

**Scripts** (advanced):
- `generate_user_guide_docx.py` - Legacy Word generator
- `scripts/build_docs.sh` - Pandoc automation
- `scripts/enhance_docx.py` - Post-processing

### What NOT to Edit

**Generated Files** (rebuild instead):
- `Panduan_Pengguna_Gateway_Config_App.docx`
- `output/*` - All generated output

**System Files**:
- `.git/` - Git internals
- `.gitignore` - Without discussion

---

## Common Tasks

### Adding a New Section

1. Determine section number
2. Update both markdown files:
   ```markdown
   ## 10. New Section Title

   Content here...

   ### 10.1 Subsection

   More content...
   ```
3. Update table of contents in both files
4. Renumber subsequent sections if needed
5. Test document generation
6. Commit with clear message

### Fixing a Typo

1. Find and fix typo
2. Check if same typo exists in other file
3. Commit:
   ```bash
   git commit -m "docs: fix typo in section 5.2"
   ```

### Adding Screenshots

1. Take screenshot (min 1080x1920 for mobile)
2. Save to `assets/ui/mobile-app/`
3. Reference in markdown:
   ```markdown
   ![BLE Scanning](assets/ui/mobile-app/ble-scanning.png)
   ```
4. Commit image with documentation

### Updating App Version

1. Update metadata in both markdown files
2. Update Python script constants
3. Regenerate documents
4. Commit all changes together

---

## Getting Help

### Resources

- **Documentation**: Read `CLAUDE.md` for comprehensive guide
- **Examples**: Review existing sections in markdown files
- **GitHub Issues**: Search existing issues for similar questions

### Contact

- **Email**: support@suriota.com
- **GitHub Issues**: [Create an issue](https://github.com/GifariKemal/SRT-MGATE-1210-User-Guide/issues)

### FAQ

**Q: Do I need to update both files?**
A: Yes, if the change affects both Indonesian and English versions.

**Q: How do I test my changes?**
A: Run `./scripts/build_docs.sh` to generate output.

**Q: Can I use AI tools for writing?**
A: Yes, but review output carefully for accuracy and tone.

**Q: What if I don't know Indonesian?**
A: Ask for help in PR description, a reviewer can assist.

**Q: How long for PR review?**
A: Usually 1-3 business days.

---

## Recognition

Contributors will be recognized in:
- `CONTRIBUTORS.md` file (if created)
- GitHub contributor graph
- Release notes (for significant contributions)

---

## License

By contributing, you agree that your contributions will be licensed under the same proprietary license as the project.

---

**Thank you for contributing to SRT-MGATE-1210 User Guide!** 🙏

For questions or clarifications, please open an issue or contact the documentation team.

---

**Last Updated**: November 30, 2025
**Maintained by**: SURIOTA Documentation Team
