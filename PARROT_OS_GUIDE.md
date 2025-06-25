# Windows Penetration Testing Tool - Parrot OS Complete Guide

## 🦜 Step-by-Step Installation on Parrot OS

### Step 1: Open Terminal
\`\`\`bash
# Open terminal (Ctrl+Alt+T or click terminal icon)
# Make sure you're in your home directory
cd ~
\`\`\`

### Step 2: Update Your System
\`\`\`bash
# Update package lists
sudo apt update

# Upgrade system (optional but recommended)
sudo apt upgrade -y
\`\`\`

### Step 3: Install Required System Tools
\`\`\`bash
# Install essential tools (most should already be installed on Parrot OS)
sudo apt install -y python3 python3-pip git nmap samba-client masscan enum4linux nbtscan curl wget

# Verify installations
python3 --version
nmap --version
smbclient --version
\`\`\`

### Step 4: Create Project Directory
\`\`\`bash
# Create a directory for penetration testing tools
mkdir -p ~/pentest-tools
cd ~/pentest-tools

# Verify you're in the right directory
pwd
# Should show: /home/yourusername/pentest-tools
\`\`\`

### Step 5: Download the Tool
\`\`\`bash
# If you have the tool files, copy them to this directory
# Or if it's in a git repository:
# git clone https://github.com/your-repo/windows-pentest-tool.git
# cd windows-pentest-tool

# For now, let's assume you have the files in the current directory
# Make sure these files exist:
ls -la main.py modules/ utils/ config/
\`\`\`

### Step 6: Install Python Dependencies
\`\`\`bash
# Install basic Python packages
pip3 install requests python-nmap

# If you have a requirements.txt file:
pip3 install -r requirements.txt

# Alternative: Install packages one by one if needed
pip3 install impacket scapy netaddr dnspython
\`\`\`

### Step 7: Run Setup Script
\`\`\`bash
# Run the setup script
python3 setup.py

# This will:
# - Check Python version
# - Create necessary directories
# - Install dependencies
# - Create default configuration
\`\`\`

### Step 8: Test Installation
\`\`\`bash
# Test the installation
python3 test_installation.py

# If everything is OK, you should see all green checkmarks
\`\`\`

### Step 9: Verify Tool Works
\`\`\`bash
# Test help command
python3 main.py --help

# Test basic functionality
python3 main.py -t 127.0.0.1 --scan-only -v
\`\`\`

## 🎯 Usage Examples on Parrot OS

### Example 1: Scan Your Local Machine
\`\`\`bash
# Basic scan of localhost
python3 main.py -t 127.0.0.1 --scan-only -v

# Expected output:
# ╔══════════════════════════════════════════════════════════════╗
# ║                Windows PenTest Tool v1.0                    ║
# ║              For Authorized Testing Only                     ║
# ╚══════════════════════════════════════════════════════════════╝
# 
# Starting reconnaissance on target: 127.0.0.1
# Discovered 1 live hosts
# Scanning ports on 127.0.0.1
# Found X open ports on 127.0.0.1
\`\`\`

### Example 2: Scan Your Home Network
\`\`\`bash
# Find your network range first
ip route show | grep -E "192\.168|10\.|172\."

# Example: If your network is 192.168.1.0/24
python3 main.py -t 192.168.1.0/24 --scan-only -v -o home_network_scan

# This will:
# - Discover all live hosts in your network
# - Scan common ports on each host
# - Generate reports in home_network_scan/ directory
\`\`\`

### Example 3: Target a Specific Windows Machine
\`\`\`bash
# Scan a specific Windows machine (replace with actual IP)
python3 main.py -t 192.168.1.100 --scan-only -v

# Full vulnerability assessment (simulation mode)
python3 main.py -t 192.168.1.100 --exploit --post-exploit -v -o windows_target_assessment
\`\`\`

### Example 4: Corporate Network Assessment (Authorized Only)
\`\`\`bash
# Large network scan (be careful with permissions!)
python3 main.py -t 10.0.0.0/24 --scan-only -v -o corporate_scan

# Full penetration test simulation
python3 main.py -t 10.0.0.0/24 --exploit --post-exploit -v -o corporate_pentest
\`\`\`

## 🔧 Command Reference

### Basic Commands
\`\`\`bash
# Help
python3 main.py --help

# Scan only (safest option)
python3 main.py -t TARGET --scan-only

# Verbose output
python3 main.py -t TARGET --scan-only -v

# Custom output directory
python3 main.py -t TARGET --scan-only -o /path/to/output

# Custom configuration
python3 main.py -t TARGET -c config/custom.json
\`\`\`

### Advanced Commands
\`\`\`bash
# Vulnerability assessment
python3 main.py -t TARGET -v

# Simulated exploitation
python3 main.py -t TARGET --exploit -v

# Full penetration test simulation
python3 main.py -t TARGET --exploit --post-exploit -v

# All options combined
python3 main.py -t 192.168.1.0/24 --exploit --post-exploit -v -o full_assessment -c config/custom.json
\`\`\`

## 📊 Understanding Results

### Console Output
\`\`\`bash
# The tool shows real-time progress:
2024-01-15 10:30:15 - Starting reconnaissance on target: 192.168.1.100
2024-01-15 10:30:16 - Discovered 1 live hosts
2024-01-15 10:30:16 - Scanning ports on 192.168.1.100
2024-01-15 10:30:20 - Found 5 open ports on 192.168.1.100
2024-01-15 10:30:21 - Analyzing vulnerabilities for 192.168.1.100
2024-01-15 10:30:22 - Found 3 potential vulnerabilities
2024-01-15 10:30:25 - Generating final report...
2024-01-15 10:30:26 - Reports generated in reports/
\`\`\`

### Report Files
\`\`\`bash
# Check generated reports
ls -la reports/

# Typical files:
# pentest_report_20240115_103025.html  <- Main report (open in browser)
# pentest_report_20240115_103025.json  <- Raw data
# pentest_report_20240115_103025.md    <- Markdown format

# View HTML report
firefox reports/pentest_report_*.html

# View in terminal
cat reports/pentest_report_*.md | less

# Parse JSON data
cat reports/pentest_report_*.json | jq '.' | less
\`\`\`

## 🛠️ Configuration

### Create Custom Configuration
\`\`\`bash
# Copy default config
cp config/default.json config/my_config.json

# Edit with your preferred editor
nano config/my_config.json
# or
gedit config/my_config.json
# or
vim config/my_config.json
\`\`\`

### Example Custom Configuration
\`\`\`json
{
  "scanning": {
    "timeout": 3,
    "threads": 100,
    "common_ports": [21, 22, 80, 135, 139, 443, 445, 3389, 5985]
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

### Use Custom Configuration
\`\`\`bash
python3 main.py -t 192.168.1.100 -c config/my_config.json --scan-only -v
\`\`\`

## 🚨 Safety and Legal Guidelines

### Before You Start
1. **Only test systems you own or have written permission to test**
2. **Set up a lab environment for practice**
3. **Understand your local laws regarding network scanning**
4. **Start with --scan-only mode**

### Recommended Lab Setup
\`\`\`bash
# Set up VirtualBox VMs for testing:
# 1. Download VirtualBox
# 2. Create Windows 10/11 VM
# 3. Create Windows Server VM
# 4. Set up isolated network
# 5. Test only against your own VMs
\`\`\`

### Safe Testing Commands
\`\`\`bash
# Always start with scan-only
python3 main.py -t YOUR_VM_IP --scan-only -v

# Test on localhost first
python3 main.py -t 127.0.0.1 --scan-only -v

# Use small network ranges
python3 main.py -t 192.168.1.100-110 --scan-only -v
\`\`\`

## 🐛 Troubleshooting on Parrot OS

### Common Issues and Solutions

#### Issue 1: "Command not found"
\`\`\`bash
# Make sure you're in the right directory
pwd
ls -la main.py

# If not found:
cd ~/pentest-tools/windows-pentest-tool
\`\`\`

#### Issue 2: "Permission denied"
\`\`\`bash
# Fix file permissions
chmod +x main.py
chmod +x setup.py
chmod +x test_installation.py
\`\`\`

#### Issue 3: "Module not found"
\`\`\`bash
# Install missing Python modules
pip3 install requests python-nmap

# Check Python path
python3 -c "import sys; print(sys.path)"

# Install in user directory if needed
pip3 install --user requests python-nmap
\`\`\`

#### Issue 4: "No hosts discovered"
\`\`\`bash
# Test network connectivity
ping -c 1 8.8.8.8

# Check your network interface
ip addr show

# Test with localhost first
python3 main.py -t 127.0.0.1 --scan-only -v
\`\`\`

#### Issue 5: "SMB enumeration failed"
\`\`\`bash
# Install SMB client tools
sudo apt install samba-client

# Test smbclient
smbclient --version
\`\`\`

### Debug Mode
\`\`\`bash
# Run with maximum verbosity
python3 main.py -t 127.0.0.1 --scan-only -v

# Check log files
tail -f pentest_*.log

# Test individual components
python3 test_installation.py
\`\`\`

## 📚 Learning Path

### Beginner (Start Here)
\`\`\`bash
# 1. Test installation
python3 test_installation.py

# 2. Scan localhost
python3 main.py -t 127.0.0.1 --scan-only -v

# 3. Scan your router
python3 main.py -t 192.168.1.1 --scan-only -v

# 4. Read the generated reports
firefox reports/pentest_report_*.html
\`\`\`

### Intermediate
\`\`\`bash
# 1. Scan your home network
python3 main.py -t 192.168.1.0/24 --scan-only -v

# 2. Enable vulnerability detection
python3 main.py -t 192.168.1.100 -v

# 3. Create custom configurations
cp config/default.json config/my_config.json
\`\`\`

### Advanced
\`\`\`bash
# 1. Full simulation mode
python3 main.py -t LAB_IP --exploit --post-exploit -v

# 2. Automate with scripts
# 3. Integrate with other tools
# 4. Modify the source code
\`\`\`

## 🔗 Integration with Other Parrot OS Tools

### Use with Nmap
\`\`\`bash
# First run nmap
nmap -sS -O 192.168.1.100

# Then run our tool
python3 main.py -t 192.168.1.100 --scan-only -v
\`\`\`

### Use with Masscan
\`\`\`bash
# Fast port scan with masscan
sudo masscan -p1-65535 192.168.1.100 --rate=1000

# Detailed analysis with our tool
python3 main.py -t 192.168.1.100 -v
\`\`\`

### Export Results
\`\`\`bash
# Export to other tools
cat reports/pentest_report_*.json | jq '.scan_results' > nmap_input.json
\`\`\`

## 📞 Getting Help

### If You're Stuck
\`\`\`bash
# 1. Run the test script
python3 test_installation.py

# 2. Check the logs
tail -f pentest_*.log

# 3. Try the minimal example
python3 -c "import socket; print('Python networking works')"

# 4. Test basic connectivity
ping -c 1 8.8.8.8
\`\`\`

### Common Parrot OS Specific Notes
- Most penetration testing tools are pre-installed
- Python3 is the default Python version
- Nmap and other tools should work out of the box
- Use `sudo` for privileged operations when needed
- The tool works best in the terminal environment
