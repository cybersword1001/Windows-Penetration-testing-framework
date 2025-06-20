# Windows Penetration Testing Tool

A comprehensive, modular penetration testing framework designed specifically for Windows environments. This tool is intended for authorized security testing and educational purposes only.

## Features

- **Automated Reconnaissance**: Network scanning and service enumeration
- **Vulnerability Detection**: Identifies common Windows vulnerabilities
- **Exploitation Framework**: Modular exploit system (simulation mode for safety)
- **Post-Exploitation**: Privilege escalation, lateral movement, and persistence checks
- **Comprehensive Reporting**: HTML, JSON, and Markdown reports
- **Modular Architecture**: Easy to extend and customize

## Platform Compatibility

### 🎯 **Target Systems**
This tool is designed to test **Windows environments** including:
- Windows Server (2008, 2012, 2016, 2019, 2022)
- Windows Desktop (7, 8, 10, 11)
- Active Directory environments
- Windows network services (SMB, RDP, LDAP, etc.)

### 💻 **Host Platform (Where the tool runs)**
The tool can run on multiple platforms:

| Platform | Status | Notes |
|----------|--------|-------|
| **Linux** | ✅ Recommended | Best compatibility with security tools |
| **Windows** | ✅ Supported | Some features may require additional setup |
| **macOS** | ⚠️ Limited | Basic functionality, some tools may be missing |

### 📦 **Installation by Platform**

#### Linux (Ubuntu/Debian)
\`\`\`bash
# Install system dependencies
sudo apt-get update
sudo apt-get install python3 python3-pip nmap samba-client

# Clone and setup
git clone <repository-url>
cd windows-pentest-tool
python3 setup.py
\`\`\`

#### Linux (CentOS/RHEL)
\`\`\`bash
# Install system dependencies
sudo yum install python3 python3-pip nmap samba-client

# Clone and setup
git clone <repository-url>
cd windows-pentest-tool
python3 setup.py
\`\`\`

#### Windows
\`\`\`powershell
# Install Python from python.org
# Download and install Nmap from https://nmap.org/download.html

# Clone and setup
git clone <repository-url>
cd windows-pentest-tool
python setup.py
\`\`\`

#### macOS
\`\`\`bash
# Install Homebrew if not already installed
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install dependencies
brew install python3 nmap samba

# Clone and setup
git clone <repository-url>
cd windows-pentest-tool
python3 setup.py
\`\`\`

## Installation

### 🐧 **For Linux (Ubuntu/Debian/Parrot OS)**

#### Step 1: Install System Dependencies
\`\`\`bash
# Update package list
sudo apt update

# Install required system tools
sudo apt install python3 python3-pip nmap samba-client git -y

# Optional: Install additional penetration testing tools
sudo apt install masscan enum4linux nbtscan -y
\`\`\`

#### Step 2: Clone the Repository
\`\`\`bash
# Clone the repository
git clone https://github.com/your-username/windows-pentest-tool.git
cd windows-pentest-tool

# Make sure you're in the correct directory
pwd
\`\`\`

#### Step 3: Install Python Dependencies
\`\`\`bash
# Install Python requirements
pip3 install -r requirements.txt

# Or use the setup script
python3 setup.py
\`\`\`

#### Step 4: Verify Installation
\`\`\`bash
# Check if all tools are available
python3 main.py --help
\`\`\`

### 🦜 **For Parrot OS (Specialized Instructions)**

Parrot OS comes with most penetration testing tools pre-installed:

\`\`\`bash
# Parrot OS usually has everything, just install Python deps
sudo apt update
pip3 install -r requirements.txt

# Verify nmap and smbclient are available (should be pre-installed)
nmap --version
smbclient --version
\`\`\`

## Usage Guide

### 🚀 **Quick Start**

#### 1. Basic Network Scan (Safe Mode)
\`\`\`bash
# Scan a single host
python3 main.py -t 192.168.1.100 --scan-only

# Scan a network range
python3 main.py -t 192.168.1.0/24 --scan-only -v
\`\`\`

#### 2. Vulnerability Assessment
\`\`\`bash
# Scan and identify vulnerabilities (no exploitation)
python3 main.py -t 192.168.1.100 -v

# Scan multiple hosts for vulnerabilities
python3 main.py -t 192.168.1.0/24 -v
\`\`\`

#### 3. Full Penetration Test (Simulation Mode)
\`\`\`bash
# Complete assessment with simulated exploitation
python3 main.py -t 192.168.1.100 --exploit --post-exploit -v

# Full network assessment
python3 main.py -t 192.168.1.0/24 --exploit --post-exploit -v -o my_pentest_report
\`\`\`

### 📋 **Command Line Options Explained**

| Option | Description | Example |
|--------|-------------|---------|
| `-t, --target` | Target IP or CIDR range (REQUIRED) | `-t 192.168.1.100` |
| `-c, --config` | Custom configuration file | `-c config/custom.json` |
| `-o, --output` | Output directory for reports | `-o /home/user/reports` |
| `-v, --verbose` | Enable detailed logging | `-v` |
| `--scan-only` | Only perform network scanning | `--scan-only` |
| `--exploit` | Enable exploitation modules (simulation) | `--exploit` |
| `--post-exploit` | Enable post-exploitation modules | `--post-exploit` |

### 🎯 **Real-World Usage Examples**

#### Example 1: Home Lab Testing
\`\`\`bash
# Test your home lab Windows machine
python3 main.py -t 192.168.1.50 --scan-only -v

# Full assessment of home lab
python3 main.py -t 192.168.1.50 --exploit --post-exploit -v -o home_lab_test
\`\`\`

#### Example 2: Corporate Network Assessment (Authorized)
\`\`\`bash
# Scan corporate network range
python3 main.py -t 10.0.0.0/24 --scan-only -v -o corporate_scan

# Full authorized penetration test
python3 main.py -t 10.0.0.0/24 --exploit --post-exploit -v -o corporate_pentest
\`\`\`

#### Example 3: Single Server Deep Dive
\`\`\`bash
# Comprehensive test of a single Windows server
python3 main.py -t 192.168.1.10 --exploit --post-exploit -v -o server_assessment
\`\`\`

### 📊 **Understanding the Output**

#### 1. Console Output
\`\`\`bash
# The tool will show real-time progress:
╔══════════════════════════════════════════════════════════════╗
║                Windows PenTest Tool v1.0                    ║
║              For Authorized Testing Only                     ║
╚══════════════════════════════════════════════════════════════╝

2024-01-15 10:30:15 - Starting reconnaissance on target: 192.168.1.100
2024-01-15 10:30:16 - Discovered 1 live hosts
2024-01-15 10:30:16 - Scanning ports on 192.168.1.100
2024-01-15 10:30:20 - Found 5 open ports on 192.168.1.100
2024-01-15 10:30:21 - Analyzing vulnerabilities for 192.168.1.100
2024-01-15 10:30:22 - Found 3 potential vulnerabilities
\`\`\`

#### 2. Generated Reports
After completion, check the `reports/` directory:
\`\`\`bash
ls -la reports/
# You'll see files like:
# pentest_report_20240115_103025.html
# pentest_report_20240115_103025.json
# pentest_report_20240115_103025.md
\`\`\`

#### 3. View Reports
\`\`\`bash
# View HTML report in browser
firefox reports/pentest_report_*.html

# View Markdown report in terminal
cat reports/pentest_report_*.md

# Parse JSON report with jq
cat reports/pentest_report_*.json | jq .
\`\`\`

### 🔧 **Configuration**

#### Custom Configuration File
\`\`\`bash
# Copy default config
cp config/default.json config/my_config.json

# Edit configuration
nano config/my_config.json

# Use custom config
python3 main.py -t 192.168.1.100 -c config/my_config.json
\`\`\`

#### Example Custom Configuration
\`\`\`json
{
  "scanning": {
    "timeout": 3,
    "threads": 100,
    "common_ports": [21, 22, 23, 25, 53, 80, 135, 139, 443, 445, 3389]
  },
  "exploitation": {
    "enabled": true,
    "safe_mode": true
  },
  "reporting": {
    "formats": ["html", "json"],
    "detailed_logs": true
  }
}
\`\`\`

### 🛡️ **Safety and Legal Usage**

#### Before Running Any Scans:
1. **Get Written Authorization**: Always have explicit written permission
2. **Test on Your Own Systems**: Start with your own lab environment
3. **Understand the Law**: Unauthorized scanning is illegal in most jurisdictions
4. **Use Safe Mode**: The tool runs in simulation mode by default

#### Recommended Test Environment Setup:
\`\`\`bash
# Set up a test lab with VirtualBox/VMware:
# 1. Install Windows 10/11 VM
# 2. Install Windows Server VM
# 3. Create isolated network
# 4. Test against your own VMs only
\`\`\`

### 🐛 **Troubleshooting**

#### Common Issues and Solutions:

1. **Permission Denied Errors**
\`\`\`bash
# Fix permissions
chmod +x main.py
sudo chown -R $USER:$USER .
\`\`\`

2. **Missing Dependencies**
\`\`\`bash
# Reinstall requirements
pip3 install -r requirements.txt --force-reinstall
\`\`\`

3. **Nmap Not Found**
\`\`\`bash
# Install nmap
sudo apt install nmap
\`\`\`

4. **SMB Enumeration Fails**
\`\`\`bash
# Install samba client tools
sudo apt install samba-client
\`\`\`

5. **Python Module Errors**
\`\`\`bash
# Check Python version (needs 3.7+)
python3 --version

# Install missing modules
pip3 install impacket scapy netaddr
\`\`\`

### 📝 **Log Files**

The tool creates detailed log files:
\`\`\`bash
# View today's log
tail -f pentest_$(date +%Y%m%d).log

# Search for errors
grep -i error pentest_*.log

# View all discovered hosts
grep -i "discovered" pentest_*.log
\`\`\`

### 🎓 **Learning and Practice**

#### Beginner Workflow:
1. Start with `--scan-only` on your own systems
2. Analyze the generated reports
3. Gradually enable vulnerability detection
4. Finally, try simulation mode with `--exploit`

#### Advanced Usage:
1. Create custom vulnerability checks
2. Modify exploitation modules
3. Integrate with other tools
4. Automate with scripts

## 🚨 **Troubleshooting - If Tool Not Running**

### Step 1: Test Your Installation
\`\`\`bash
# Run the installation test
python3 test_installation.py

# This will check:
# - Python version
# - Required files
# - System tools
# - Basic functionality
\`\`\`

### Step 2: Common Fixes

#### Problem: "ModuleNotFoundError"
\`\`\`bash
# Fix: Install missing Python modules
pip3 install requests
pip3 install python-nmap

# Or install all at once
pip3 install -r requirements.txt
\`\`\`

#### Problem: "Permission denied"
\`\`\`bash
# Fix: Make files executable
chmod +x main.py
chmod +x setup.py
chmod +x test_installation.py
\`\`\`

#### Problem: "No such file or directory"
\`\`\`bash
# Fix: Make sure you're in the right directory
pwd
ls -la main.py

# If main.py is not there, you're in the wrong directory
cd /path/to/windows-pentest-tool
\`\`\`

#### Problem: Tool starts but finds no hosts
\`\`\`bash
# Test with localhost first
python3 main.py -t 127.0.0.1 --scan-only -v

# Test ping manually
ping -c 1 192.168.1.1

# Check your network range
ip route show  # Linux
route -n       # Linux alternative
\`\`\`

### Step 3: Manual Installation Check
\`\`\`bash
# 1. Check Python version
python3 --version

# 2. Check if files exist
ls -la main.py modules/ utils/ config/

# 3. Test basic Python import
python3 -c "import socket, threading, subprocess; print('Basic modules OK')"

# 4. Test the tool help
python3 main.py --help
\`\`\`

### Step 4: Minimal Working Example
\`\`\`bash
# If everything else fails, try this minimal test:
python3 -c "
import socket
s = socket.socket()
s.settimeout(1)
try:
    s.connect(('127.0.0.1', 22))
    print('Port 22 open on localhost')
except:
    print('Port 22 closed on localhost')
s.close()
"
\`\`\`

### Step 5: Get Detailed Error Information
\`\`\`bash
# Run with maximum verbosity to see what's failing
python3 main.py -t 127.0.0.1 --scan-only -v

# Check the log file
tail -f pentest_*.log
\`\`\`

### Step 6: Platform-Specific Issues

#### Ubuntu/Debian:
\`\`\`bash
sudo apt update
sudo apt install python3 python3-pip nmap
pip3 install requests
\`\`\`

#### Parrot OS:
\`\`\`bash
# Usually everything is pre-installed, just run:
pip3 install requests
\`\`\`

#### CentOS/RHEL:
\`\`\`bash
sudo yum install python3 python3-pip nmap
pip3 install requests
\`\`\`

### Step 7: If Still Not Working
\`\`\`bash
# Create a simple test to isolate the problem:
cat > simple_test.py << 'EOF'
#!/usr/bin/env python3
import socket
import sys

def test_port(host, port):
    try:
        s = socket.socket()
        s.settimeout(2)
        result = s.connect_ex((host, port))
        s.close()
        return result == 0
    except:
        return False

if len(sys.argv) != 3:
    print("Usage: python3 simple_test.py <host> <port>")
    sys.exit(1)

host = sys.argv[1]
port = int(sys.argv[2])

if test_port(host, port):
    print(f"✅ Port {port} is open on {host}")
else:
    print(f"❌ Port {port} is closed on {host}")
EOF

# Test it:
python3 simple_test.py 127.0.0.1 22
python3 simple_test.py google.com 80
