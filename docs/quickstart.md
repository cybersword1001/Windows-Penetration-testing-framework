# Quick Start Guide

Get up and running with VulnScan Pentest Pro in 5 minutes.

## Installation

\`\`\`bash
# Update system
sudo apt update

# Install dependencies
sudo apt install python3 python3-pip nmap samba-client -y

# Clone repository
git clone https://github.com/cybersword1001/windows-penetration-testing-tool.git
cd windows-penetration-testing-tool

# Install Python dependencies
pip3 install -r requirements.txt
\`\`\`

## First Run

\`\`\`bash
# See the professional banner
python3 main.py --help

# Scan localhost (safest first test)
python3 main.py -t 127.0.0.1 --scan-only -v

# Scan your router
python3 main.py -t 192.168.1.1 --scan-only -v
\`\`\`

## Common Commands

| Task | Command |
|------|---------|
| Show version | `python3 main.py --version` |
| Show help | `python3 main.py --help` |
| Scan a host | `python3 main.py -t 192.168.1.100 --scan-only -v` |
| Full assessment | `python3 main.py -t 192.168.1.100 --exploit --post-exploit -v` |
| Scan network | `python3 main.py -t 192.168.1.0/24 --scan-only -v` |
| Custom output | `python3 main.py -t 192.168.1.100 --scan-only -o my_results` |

## Next Steps

- Read `docs/usage.md` for detailed documentation
- Check `examples/example_run.txt` for sample output
- Review reports in the `reports/` directory
