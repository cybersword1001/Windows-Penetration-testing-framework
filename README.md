# VulnScan Pentest Pro

[![Python 3.7+](https://img.shields.io/badge/python-3.7%2B-blue)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Build Status](https://img.shields.io/badge/build-passing-brightgreen)](#)

A comprehensive, modular penetration testing framework designed specifically for **authorized Windows security testing** and educational purposes.

## Quick Start

### Installation (3 steps)

\`\`\`bash
# 1. Install system dependencies
sudo apt update && sudo apt install -y python3 python3-pip nmap samba-client

# 2. Clone and navigate
git clone https://github.com/cybersword1001/windows-penetration-testing-tool.git
cd windows-penetration-testing-tool

# 3. Install Python dependencies
pip3 install -r requirements.txt
\`\`\`

### Run the Tool

\`\`\`bash
# Display banner and start tool
python3 main.py --help

# Run a basic network scan
python3 main.py -t 192.168.1.1 --scan-only -v

# Full assessment with simulated exploitation
python3 main.py -t 192.168.1.100 --exploit --post-exploit -v
\`\`\`

## Features

- **Automated Reconnaissance**: Network scanning, host discovery, and service enumeration
- **Vulnerability Detection**: Identifies common Windows flaws (EternalBlue, SMBv1, weak configs)
- **Exploitation Framework**: Modular exploit system (simulation mode for safety)
- **Post-Exploitation**: Privilege escalation, lateral movement, and persistence checks
- **Comprehensive Reporting**: HTML, JSON, and Markdown format reports
- **Modular Architecture**: Easy to extend with custom modules
- **Professional Startup Banner**: Displays system info and module status on launch

## Usage Examples

### Example 1: Scan Only (No Exploitation)
\`\`\`bash
python3 main.py -t 192.168.1.100 --scan-only -v
\`\`\`
**Output:**
\`\`\`
[+] Scanning target: 192.168.1.100
[+] Found 5 open ports
[+] Identified services: SMB, RDP, HTTP
[+] Report saved to: reports/pentest_report_*.html
\`\`\`

### Example 2: Full Assessment (With Simulated Exploits)
\`\`\`bash
python3 main.py -t 192.168.1.100 --exploit --post-exploit -v -o my_assessment
\`\`\`

### Example 3: Network Range Assessment
\`\`\`bash
python3 main.py -t 192.168.1.0/24 --scan-only -v
\`\`\`

### Example 4: Check Version
\`\`\`bash
python3 main.py --version
# Output: VulnScan Pentest Pro v0
\`\`\`

## Configuration

### Default Configuration File
Located at `config/default.json`:

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
    "formats": ["html", "json", "markdown"],
    "detailed_logs": true
  }
}
\`\`\`

### Using Custom Configuration
\`\`\`bash
cp config/default.json config/custom.json
# Edit config/custom.json
python3 main.py -t 192.168.1.100 -c config/custom.json
\`\`\`

## Structure

\`\`\`
windows-penetration-tool/
├── main.py                 # Main entry point with banner and CLI
├── version.py              # Version and metadata
├── requirements.txt        # Python dependencies
├── modules/                # Core scanning and exploitation modules
│   ├── scanner.py          # Network scanning engine
│   ├── vulnerability_detector.py
│   ├── exploiter.py
│   ├── post_exploit.py
│   └── reporter.py
├── utils/                  # Utility modules
│   ├── logger.py           # Logging configuration
│   └── config.py           # Configuration management
├── config/                 # Configuration files
│   └── default.json
├── docs/                   # Documentation
│   ├── quickstart.md
│   └── usage.md
├── examples/               # Example runs and outputs
│   └── example_run.txt
└── .github/workflows/      # CI/CD configuration
    └── basic-check.yml
\`\`\`

## Contributing

We welcome contributions! Please follow these guidelines:

1. **Report Issues**: Open a GitHub issue describing the problem
2. **Submit PRs**: Fork the repo, create a feature branch, and submit a pull request
3. **Code Style**: Follow PEP 8 standards
4. **Testing**: Run `python3 test_installation.py` before submitting PR

Example contribution workflow:
\`\`\`bash
git clone https://github.com/cybersword1001/windows-penetration-testing-tool.git
git checkout -b feature/my-feature
# Make your changes
git commit -m "feat: add new feature"
git push origin feature/my-feature
# Open a pull request
\`\`\`

## License

This project is licensed under the **MIT License** - see [LICENSE](LICENSE) file for details.

## Author

**Created by:** [CYBERSWORD1001](https://github.com/cybersword1001)

A security researcher passionate about penetration testing, Windows security, and open-source security tools.

## Legal Disclaimer

**This tool is for authorized security testing and educational purposes only.**

- Unauthorized access to computer systems is illegal
- Always obtain written permission before testing
- Use this tool responsibly and ethically
- The authors are not liable for misuse

## Safety Guidelines

- ✅ Test on your own systems first
- ✅ Get explicit written authorization
- ✅ Use safe mode (default)
- ✅ Start with `--scan-only`
- ❌ Never scan without permission
- ❌ Never use on production systems without authorization

## Troubleshooting

### Issue: "vite is not recognized" or Python module errors
\`\`\`bash
pip3 install -r requirements.txt --upgrade
\`\`\`

### Issue: "Permission denied"
\`\`\`bash
chmod +x main.py
sudo chown -R $USER:$USER .
\`\`\`

### Issue: Nmap not found
\`\`\`bash
sudo apt install nmap
\`\`\`

### Issue: No hosts discovered
\`\`\`bash
# Test with localhost first
python3 main.py -t 127.0.0.1 --scan-only -v
\`\`\`

## Support

- 📖 Read [docs/quickstart.md](docs/quickstart.md) for quick help
- 📖 Read [docs/usage.md](docs/usage.md) for detailed usage
- 🐛 Open a GitHub issue for bugs
- 💬 Check discussions for general questions
