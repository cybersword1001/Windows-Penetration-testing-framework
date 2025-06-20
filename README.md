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

1. Clone or download this repository
2. Install required Python packages:
   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

## Usage

### Basic Scanning
\`\`\`bash
python main.py -t 192.168.1.100 --scan-only
\`\`\`

### Full Assessment (Simulation Mode)
\`\`\`bash
python main.py -t 192.168.1.0/24 --exploit --post-exploit -v
\`\`\`

### Custom Configuration
\`\`\`bash
python main.py -t 192.168.1.100 -c config/custom.json -o custom_reports
\`\`\`

## Command Line Options

- `-t, --target`: Target IP or CIDR range (required)
- `-c, --config`: Configuration file (default: config/default.json)
- `-o, --output`: Output directory for reports (default: reports)
- `-v, --verbose`: Enable verbose logging
- `--scan-only`: Perform scanning only
- `--exploit`: Enable exploitation modules (simulation mode)
- `--post-exploit`: Enable post-exploitation modules

## Safety Features

- **Simulation Mode**: All exploits run in simulation mode by default
- **Authorization Checks**: Built-in warnings about authorized use only
- **Detailed Logging**: Comprehensive logging for audit trails
- **Safe Defaults**: Conservative settings to prevent accidental damage

## Legal Disclaimer

⚠️ **IMPORTANT**: This tool is designed for authorized penetration testing and educational purposes only. 

- Only use this tool on systems you own or have explicit written permission to test
- Unauthorized access to computer systems is illegal in most jurisdictions
- The authors are not responsible for any misuse of this tool
- Always follow responsible disclosure practices

## Architecture

\`\`\`
windows-pentest-tool/
├── main.py                 # Main entry point
├── modules/
│   ├── scanner.py         # Network scanning and enumeration
│   ├── vulnerability_detector.py  # Vulnerability identification
│   ├── exploiter.py       # Exploitation framework
│   ├── post_exploit.py    # Post-exploitation modules
│   └── reporter.py        # Report generation
├── utils/
│   ├── logger.py          # Logging utilities
│   └── config.py          # Configuration management
├── config/
│   └── default.json       # Default configuration
└── reports/               # Generated reports directory
\`\`\`

## Extending the Tool

### Adding New Vulnerability Checks

1. Add a new method to `VulnerabilityDetector` class
2. Register the check in the `vulnerability_checks` list
3. Follow the existing pattern for vulnerability data structure

### Adding New Exploits

1. Add a new method to `ExploitManager` class
2. Register the exploit in the `exploits` dictionary
3. Ensure all exploits run in simulation mode for safety

### Custom Reporting

The reporting module supports multiple formats and can be extended to include additional report types or custom formatting.

## Configuration

The tool uses JSON configuration files to customize behavior:

- **Scanning**: Timeouts, thread counts, port lists
- **Exploitation**: Safety settings, attempt limits
- **Reporting**: Output formats, detail levels
- **Legal**: Disclaimer and authorization requirements

## Educational Integration

This tool is designed to integrate with educational platforms like Versal.ai:

- **Interactive Labs**: Embedded terminal sessions
- **Guided Exercises**: Step-by-step penetration testing tutorials
- **Assessment Integration**: Automated validation of user actions
- **Visualization**: Attack path diagrams and result visualization

## Contributing

Contributions are welcome! Please ensure all contributions:

- Maintain the educational and authorized-use focus
- Include appropriate safety measures
- Follow the existing code structure and documentation standards
- Include tests for new functionality

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For questions, issues, or contributions, please open an issue on the project repository.
