# Windows Penetration Tool (CLI)

This is the backend Python command-line tool for performing actual penetration testing tasks.

## Prerequisites
- Python 3.8+
- Nmap (installed and in system PATH)
- Linux/Parrot OS (Recommended) or Windows

## Installation

1.  Navigate to this directory:
    \`\`\`bash
    cd python-tool
    \`\`\`

2.  Install dependencies:
    \`\`\`bash
    pip install -r requirements.txt
    \`\`\`

## Usage

### Basic Scan
\`\`\`bash
python main.py -t <TARGET_IP> --scan-only -v
\`\`\`

### Full Simulation (Safe Mode)
\`\`\`bash
python main.py -t <TARGET_IP> --exploit --post-exploit -v
\`\`\`

### Options
- `-t`, `--target`: Target IP address
- `--scan-only`: Run only the network scanner
- `--exploit`: Attempt exploitation (simulated by default)
- `--post-exploit`: Run post-exploitation modules
- `-v`: Verbose output
