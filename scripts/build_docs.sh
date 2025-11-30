#!/bin/bash
#
# build_docs.sh - Multi-format documentation builder
#
# Builds user guide documentation in multiple formats using Pandoc
# Supports: DOCX, PDF, HTML
#
# Usage: ./scripts/build_docs.sh [options]
#
# Options:
#   --docx-only    Build only DOCX output
#   --pdf-only     Build only PDF output
#   --html-only    Build only HTML output
#   --all          Build all formats (default)
#   --clean        Clean output directory before build
#   --help         Show this help message
#
# Author: SURIOTA Documentation Team
# Version: 1.0
# Date: November 30, 2025

set -e  # Exit on error

# Color codes for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Configuration
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"
INPUT_MD_ID="USER_GUIDE_CLEAN.md"
INPUT_MD_EN="USER_GUIDE_MOBILE_APP.md"
TEMPLATE="assets/templates/suriota-template.docx"
OUTPUT_DIR="output"
BUILD_DATE=$(date +'%d %B %Y')

# Default values
BUILD_DOCX=true
BUILD_PDF=true
BUILD_HTML=true
CLEAN_OUTPUT=false

# Functions
print_header() {
    echo -e "${BLUE}════════════════════════════════════════════════════${NC}"
    echo -e "${BLUE}   SRT-MGATE-1210 Documentation Builder v1.0${NC}"
    echo -e "${BLUE}════════════════════════════════════════════════════${NC}"
    echo ""
}

print_success() {
    echo -e "${GREEN}✓${NC} $1"
}

print_error() {
    echo -e "${RED}✗${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}⚠${NC} $1"
}

print_info() {
    echo -e "${BLUE}ℹ${NC} $1"
}

check_dependencies() {
    print_info "Checking dependencies..."

    local missing_deps=()

    # Check pandoc
    if ! command -v pandoc &> /dev/null; then
        missing_deps+=("pandoc")
    else
        print_success "Pandoc $(pandoc --version | head -n1 | awk '{print $2}')"
    fi

    # Check pdflatex for PDF generation
    if [[ "$BUILD_PDF" == true ]]; then
        if ! command -v xelatex &> /dev/null && ! command -v pdflatex &> /dev/null; then
            missing_deps+=("texlive (for PDF generation)")
        else
            print_success "LaTeX engine found"
        fi
    fi

    # Report missing dependencies
    if [ ${#missing_deps[@]} -ne 0 ]; then
        print_error "Missing dependencies:"
        for dep in "${missing_deps[@]}"; do
            echo "  - $dep"
        done
        echo ""
        print_info "Install on Ubuntu/Debian:"
        echo "  sudo apt install pandoc texlive-latex-recommended texlive-fonts-recommended texlive-latex-extra"
        echo ""
        exit 1
    fi

    echo ""
}

clean_output_directory() {
    if [[ "$CLEAN_OUTPUT" == true ]]; then
        print_info "Cleaning output directory..."
        rm -rf "$OUTPUT_DIR"/*
        print_success "Output directory cleaned"
        echo ""
    fi
}

create_output_directory() {
    if [ ! -d "$OUTPUT_DIR" ]; then
        mkdir -p "$OUTPUT_DIR"
        print_success "Created output directory: $OUTPUT_DIR"
        echo ""
    fi
}

build_docx() {
    local input_file="$1"
    local output_name="$2"
    local language="$3"

    print_info "Building DOCX: $output_name..."

    # Check if template exists
    local template_arg=""
    if [ -f "$TEMPLATE" ]; then
        template_arg="--reference-doc=$TEMPLATE"
        print_info "Using template: $TEMPLATE"
    else
        print_warning "Template not found, using default styling"
    fi

    # Build DOCX
    pandoc "$input_file" \
        --from=markdown+smart \
        --to=docx \
        $template_arg \
        --toc \
        --toc-depth=3 \
        --number-sections \
        --metadata title="Panduan Pengguna Gateway Config App" \
        --metadata author="Tim Dokumentasi SURIOTA" \
        --metadata date="$BUILD_DATE" \
        --metadata lang="$language" \
        -o "$OUTPUT_DIR/$output_name"

    if [ $? -eq 0 ]; then
        local size=$(du -h "$OUTPUT_DIR/$output_name" | cut -f1)
        print_success "DOCX generated: $output_name ($size)"
    else
        print_error "Failed to generate DOCX: $output_name"
        return 1
    fi
}

build_pdf() {
    local input_file="$1"
    local output_name="$2"

    print_info "Building PDF: $output_name..."

    # Determine PDF engine
    local pdf_engine="xelatex"
    if ! command -v xelatex &> /dev/null; then
        pdf_engine="pdflatex"
        print_warning "XeLaTeX not found, using pdflatex (limited font support)"
    fi

    # Build PDF
    pandoc "$input_file" \
        --from=markdown+smart \
        --pdf-engine="$pdf_engine" \
        --toc \
        --toc-depth=3 \
        --number-sections \
        -V geometry:margin=2.5cm \
        -V mainfont="Calibri" \
        -V fontsize=11pt \
        -V papersize=a4 \
        --metadata title="Panduan Pengguna Gateway Config App" \
        --metadata author="Tim Dokumentasi SURIOTA" \
        --metadata date="$BUILD_DATE" \
        -o "$OUTPUT_DIR/$output_name" 2>&1 | grep -v "^$"

    if [ ${PIPESTATUS[0]} -eq 0 ]; then
        local size=$(du -h "$OUTPUT_DIR/$output_name" | cut -f1)
        print_success "PDF generated: $output_name ($size)"
    else
        print_error "Failed to generate PDF: $output_name"
        return 1
    fi
}

build_html() {
    local input_file="$1"
    local output_name="$2"

    print_info "Building HTML: $output_name..."

    # Build HTML
    pandoc "$input_file" \
        --from=markdown+smart \
        --to=html5 \
        --standalone \
        --toc \
        --toc-depth=3 \
        --number-sections \
        --css=style.css \
        --metadata title="Panduan Pengguna Gateway Config App" \
        --metadata author="Tim Dokumentasi SURIOTA" \
        --metadata date="$BUILD_DATE" \
        --highlight-style=tango \
        -o "$OUTPUT_DIR/$output_name"

    if [ $? -eq 0 ]; then
        local size=$(du -h "$OUTPUT_DIR/$output_name" | cut -f1)
        print_success "HTML generated: $output_name ($size)"
    else
        print_error "Failed to generate HTML: $output_name"
        return 1
    fi
}

show_help() {
    cat << EOF
Usage: ./scripts/build_docs.sh [OPTIONS]

Multi-format documentation builder for SRT-MGATE-1210 User Guide

OPTIONS:
    --docx-only     Build only DOCX output
    --pdf-only      Build only PDF output
    --html-only     Build only HTML output
    --all           Build all formats (default)
    --clean         Clean output directory before build
    --help          Show this help message

EXAMPLES:
    # Build all formats
    ./scripts/build_docs.sh

    # Build only DOCX
    ./scripts/build_docs.sh --docx-only

    # Clean and build all
    ./scripts/build_docs.sh --clean --all

OUTPUT:
    All files are saved to: output/

    Generated files:
    - Panduan_Gateway_Config_App_ID.docx  (Indonesian DOCX)
    - Panduan_Gateway_Config_App_EN.docx  (English DOCX)
    - Panduan_Gateway_Config_App_ID.pdf   (Indonesian PDF)
    - Panduan_Gateway_Config_App_EN.pdf   (English PDF)
    - Panduan_Gateway_Config_App_ID.html  (Indonesian HTML)
    - Panduan_Gateway_Config_App_EN.html  (English HTML)

REQUIREMENTS:
    - pandoc (>= 2.0)
    - texlive-latex-recommended (for PDF)
    - texlive-fonts-recommended (for PDF)

INSTALLATION (Ubuntu/Debian):
    sudo apt install pandoc texlive-latex-recommended texlive-fonts-recommended

EOF
}

# Parse command line arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        --docx-only)
            BUILD_DOCX=true
            BUILD_PDF=false
            BUILD_HTML=false
            shift
            ;;
        --pdf-only)
            BUILD_DOCX=false
            BUILD_PDF=true
            BUILD_HTML=false
            shift
            ;;
        --html-only)
            BUILD_DOCX=false
            BUILD_PDF=false
            BUILD_HTML=true
            shift
            ;;
        --all)
            BUILD_DOCX=true
            BUILD_PDF=true
            BUILD_HTML=true
            shift
            ;;
        --clean)
            CLEAN_OUTPUT=true
            shift
            ;;
        --help|-h)
            show_help
            exit 0
            ;;
        *)
            print_error "Unknown option: $1"
            echo "Use --help for usage information"
            exit 1
            ;;
    esac
done

# Main execution
main() {
    cd "$PROJECT_ROOT"

    print_header
    check_dependencies
    clean_output_directory
    create_output_directory

    local build_count=0
    local success_count=0

    # Build Indonesian documentation
    print_info "Building Indonesian documentation..."
    echo ""

    if [[ "$BUILD_DOCX" == true ]]; then
        ((build_count++))
        if build_docx "$INPUT_MD_ID" "Panduan_Gateway_Config_App_ID.docx" "id-ID"; then
            ((success_count++))
        fi
        echo ""
    fi

    if [[ "$BUILD_PDF" == true ]]; then
        ((build_count++))
        if build_pdf "$INPUT_MD_ID" "Panduan_Gateway_Config_App_ID.pdf"; then
            ((success_count++))
        fi
        echo ""
    fi

    if [[ "$BUILD_HTML" == true ]]; then
        ((build_count++))
        if build_html "$INPUT_MD_ID" "Panduan_Gateway_Config_App_ID.html"; then
            ((success_count++))
        fi
        echo ""
    fi

    # Build English documentation
    print_info "Building English documentation..."
    echo ""

    if [[ "$BUILD_DOCX" == true ]]; then
        ((build_count++))
        if build_docx "$INPUT_MD_EN" "Panduan_Gateway_Config_App_EN.docx" "en-US"; then
            ((success_count++))
        fi
        echo ""
    fi

    if [[ "$BUILD_PDF" == true ]]; then
        ((build_count++))
        if build_pdf "$INPUT_MD_EN" "Panduan_Gateway_Config_App_EN.pdf"; then
            ((success_count++))
        fi
        echo ""
    fi

    if [[ "$BUILD_HTML" == true ]]; then
        ((build_count++))
        if build_html "$INPUT_MD_EN" "Panduan_Gateway_Config_App_EN.html"; then
            ((success_count++))
        fi
        echo ""
    fi

    # Summary
    echo -e "${BLUE}════════════════════════════════════════════════════${NC}"
    echo -e "${GREEN}Build Summary:${NC}"
    echo -e "  Total builds: $build_count"
    echo -e "  Successful: ${GREEN}$success_count${NC}"
    echo -e "  Failed: ${RED}$((build_count - success_count))${NC}"
    echo ""
    echo -e "Output directory: ${BLUE}$OUTPUT_DIR/${NC}"
    echo -e "${BLUE}════════════════════════════════════════════════════${NC}"

    if [ $success_count -eq $build_count ]; then
        exit 0
    else
        exit 1
    fi
}

# Run main function
main
