#!/bin/bash
# Windows Penetration Testing Tool - Parrot OS Setup Script

echo "🦜 Windows Penetration Testing Tool - Parrot OS Setup"
echo "=================================================="

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${GREEN}[✓]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[!]${NC} $1"
}

print_error() {
    echo -e "${RED}[✗]${NC} $1"
}

print_info() {
    echo -e "${BLUE}[i]${NC} $1"
}

# Step 1: Check if running on Parrot OS
print_info "Checking operating system..."
if grep -q "Parrot" /etc/os-release 2>/dev/null; then
    print_status "Parrot OS detected"
else
    print_warning "This script is optimized for Parrot OS but should work on Debian-based systems"
fi

# Step 2: Update system
print_info "Updating package lists..."
sudo apt update

# Step 3: Install required system packages
print_info "Installing required system packages..."
sudo apt install -y python3 python3-pip git nmap samba-client masscan enum4linux nbtscan

# Step 4: Check Python version
print_info "Checking Python version..."
PYTHON_VERSION=$(python3 --version 2>&1 | cut -d' ' -f2 | cut -d'.' -f1,2)
if python3 -c "import sys; exit(0 if sys.version_info >= (3,7) else 1)"; then
    print_status "Python version is compatible: $(python3 --version)"
else
    print_error "Python 3.7+ required. Current version: $(python3 --version)"
    exit 1
fi

# Step 5: Install Python packages
print_info "Installing Python packages..."
pip3 install requests python-nmap

# Step 6: Create project directory
print_info "Setting up project directory..."
mkdir -p ~/pentest-tools
cd ~/pentest-tools

# Step 7: Make script executable
chmod +x parrot_os_setup.sh

print_status "Setup completed successfully!"
print_info "Next steps:"
echo "1. Download or clone the Windows Penetration Testing Tool"
echo "2. Run: python3 setup.py"
echo "3. Test with: python3 main.py -t 127.0.0.1 --scan-only -v"
