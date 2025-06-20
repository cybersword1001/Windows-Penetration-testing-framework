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
        print(f"Current version: {sys.version}")
        return False
    print(f"✅ Python {sys.version.split()[0]} detected")
    return True

def create_directories():
    """Create necessary directories"""
    directories = ['reports', 'logs', 'config']
    
    print("📁 Creating directories...")
    for directory in directories:
        Path(directory).mkdir(exist_ok=True)
        print(f"✅ Created {directory}/ directory")

def create_default_config():
    """Create default configuration file if it doesn't exist"""
    config_file = Path('config/default.json')
    if not config_file.exists():
        print("📝 Creating default configuration...")
        default_config = {
            "scanning": {
                "timeout": 5,
                "threads": 50,
                "common_ports": [21, 22, 23, 25, 53, 80, 110, 135, 139, 143, 443, 445, 993, 995, 1723, 3306, 3389, 5432, 5900, 8080],
                "ping_timeout": 1000,
                "service_detection": True
            },
            "exploitation": {
                "enabled": False,
                "safe_mode": True,
                "max_attempts": 3,
                "delay_between_attempts": 1
            },
            "post_exploitation": {
                "enabled": False,
                "privilege_escalation": True,
                "credential_dumping": False,
                "lateral_movement": False,
                "persistence": False
            },
            "reporting": {
                "formats": ["html", "json", "markdown"],
                "include_screenshots": False,
                "output_directory": "reports",
                "detailed_logs": True
            },
            "legal": {
                "disclaimer": "This tool is for authorized penetration testing only. Unauthorized use is illegal.",
                "require_authorization": True
            }
        }
        
        import json
        with open(config_file, 'w') as f:
            json.dump(default_config, f, indent=2)
        print("✅ Default configuration created")

def install_basic_requirements():
    """Install basic Python requirements"""
    print("📦 Installing basic Python dependencies...")
    
    basic_packages = [
        'requests',
    ]
    
    for package in basic_packages:
        try:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])
            print(f"✅ Installed {package}")
        except subprocess.CalledProcessError:
            print(f"⚠️  Failed to install {package} (optional)")

def check_system_tools():
    """Check for system tools"""
    print("🔍 Checking system tools...")
    
    tools = ['ping']
    optional_tools = ['nmap', 'smbclient']
    
    for tool in tools:
        try:
            subprocess.run([tool, '--version'], capture_output=True, timeout=5)
            print(f"✅ {tool} available")
        except (subprocess.TimeoutExpired, FileNotFoundError):
            print(f"❌ {tool} not found")
    
    for tool in optional_tools:
        try:
            subprocess.run([tool, '--version'], capture_output=True, timeout=5)
            print(f"✅ {tool} available (optional)")
        except (subprocess.TimeoutExpired, FileNotFoundError):
            print(f"⚠️  {tool} not found (optional)")

def make_executable():
    """Make main.py executable"""
    if platform.system() != 'windows':
        try:
            os.chmod('main.py', 0o755)
            print("✅ Made main.py executable")
        except Exception as e:
            print(f"⚠️  Could not make main.py executable: {e}")

def display_usage():
    """Display usage information"""
    print("""
🎯 Windows Penetration Testing Tool Setup Complete!

📋 Quick Test:
   python3 test_installation.py

📋 Usage Examples:
   Basic scan:     python3 main.py -t 192.168.1.100 --scan-only -v
   Full test:      python3 main.py -t 192.168.1.0/24 --exploit --post-exploit -v

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
    
    if not check_python_version():
        sys.exit(1)
    
    create_directories()
    create_default_config()
    install_basic_requirements()
    check_system_tools()
    make_executable()
    
    print("=" * 60)
    print("✅ Setup completed!")
    display_usage()

if __name__ == "__main__":
    main()
