#!/bin/bash
# OUROLANG BUILD & INSTALL SCRIPT
# Sets up OuroLang environment and makes scripts executable

set -e

echo "╔══════════════════════════════════════╗"
echo "║   OuroLang Setup & Configuration    ║"
echo "╚══════════════════════════════════════╝"
echo ""

# Check requirements
echo "🔍 Checking system requirements..."

if ! command -v gcc &> /dev/null; then
    echo "⚠️  Warning: GCC not found (optional, needed for VM compilation)"
fi

if ! command -v bash &> /dev/null; then
    echo "❌ Error: Bash not found (required)"
    exit 1
fi

# Create necessary directories
echo "📁 Creating directories..."
mkdir -p bin build stable

# Make scripts executable
echo "🔐 Making scripts executable..."
chmod +x ouroc ouroi ouro ouro_run 2>/dev/null || true

# Make native binaries executable if they exist
if [ -f "./native/kernel_compiler" ]; then
    chmod +x ./native/kernel_compiler
    echo "✅ kernel_compiler is ready"
fi

if [ -f "./native/vm_arm64" ]; then
    chmod +x ./native/vm_arm64
    echo "✅ vm_arm64 is ready"
fi

if [ -f "./native/ouro_shell" ]; then
    chmod +x ./native/ouro_shell
    echo "✅ ouro_shell is ready"
fi

# Compile VM if source exists
if [ -f "src/vm/ouro_vm_portable.c" ] && [ ! -f "bin/ouro_vm" ]; then
    echo ""
    echo "🔨 Compiling VM from source..."
    if command -v make &> /dev/null; then
        make vm || echo "⚠️  VM compilation skipped (make failed)"
    else
        echo "⚠️  Make not found, VM compilation skipped"
    fi
elif [ -f "bin/ouro_vm" ]; then
    echo "✅ VM already compiled"
fi

echo ""
echo "╔══════════════════════════════════════╗"
echo "║   ✅ Setup Complete!                ║"
echo "╚══════════════════════════════════════╝"
echo ""
echo "Next steps:"
echo "  • Run example:  ./ouro run apps/halo.ouro"
echo "  • Shell:        ./native/ouro_shell"
echo "  • Compile:      ./ouroc program.ouro"
echo "  • Get help:     ./ouro help"
echo ""
