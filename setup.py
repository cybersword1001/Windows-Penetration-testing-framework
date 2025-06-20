#!/usr/bin/env python3
"""
Setup script for Windows Penetration Testing Tool
"""

import os
import sys
import platform
import subprocess
from pathlib import Path

def check_python_version():
    """Check if Python version is compatible"""
    if sys.version_info < (3, 7):
        print("❌ Python 3.7 or higher is required")
        sys.exit(1)
    print(f"✅ Python {sys.version.split()[0]} detected")

def install_requirements():
    """Install Python requirements"""
    print("📦 Installing Python dependencies...")
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])
        print("✅ Python dependencies installed successfully")
    except subprocess.CalledProcessError:
        print("❌ Failed to install Python dependencies")
        sys.exit(1)

def check_system_tools():
    """Check for required system tools"""
    tools = {
        'nmap': 'Network scanning',
        'ping': 'Host discovery'
    }
    
    if platform.system().lower() != 'windows':
        tools['smbclient'] = 'SMB enumeration'
    
    print("🔍 Checking system tools...")
    missing_tools = []
    
    for tool, description in tools.items():
        try:
            subprocess.run([tool, '--version'], capture_output=True, timeout=5)
            print(f"✅ {tool} - {description}")
        except (subprocess.TimeoutExpired, FileNotFoundError):
            print(f"❌ {tool} - {description} (MISSING)")
            missing_tools.append(tool)
    
    if missing_tools:
        print(f"\n⚠️  Missing tools: {', '.join(missing_tools)}")
        print("Please install missing tools using your system package manager:")
        
        if platform.system().lower() == 'linux':
            print("Ubuntu/Debian: sudo apt-get install nmap samba-client")
            print("CentOS/RHEL: sudo yum install nmap samba-client")
        elif platform.system().lower() == 'darwin':
            print("macOS: brew install nmap samba")
        elif platform.system().lower() == 'windows':
            print("Windows: Download nmap from https://nmap.org/download.html")

def create_directories():
    """Create necessary directories"""
    directories = ['reports', 'logs', 'config']
    
    print("📁 Creating directories...")
    for directory in directories:
        Path(directory).mkdir(exist_ok=True)
        print(f"✅ Created {directory}/ directory")

def display_usage():
    """Display usage information"""
    print("""
🎯 Windows Penetration Testing Tool Setup Complete!

📋 Usage Examples:
   Basic scan:     python main.py -t 192.168.1.100 --scan-only
   Full test:      python main.py -t 192.168.1.0/24 --exploit --post-exploit -v
   Custom config:  python main.py -t 192.168.1.100 -c config/custom.json

⚠️  Legal Notice:
   This tool is for AUTHORIZED testing only!
   Only use on systems you own or have explicit permission to test.

📚 Documentation:
   See README.md for detailed usage instructions.
""")

def main():
    """Main setup function"""
    print("🔧 Setting up Windows Penetration Testing Tool...")
    print("=" * 60)
    
    check_python_version()
    create_directories()
    install_requirements()
    check_system_tools()
    
    print("=" * 60)
    print("✅ Setup completed successfully!")
    display_usage()

if __name__ == "__main__":
    main()
