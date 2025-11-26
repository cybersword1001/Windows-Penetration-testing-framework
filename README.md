# 🚀 VulnScan Pentest Pro

[![Python 3.7+](https://img.shields.io/badge/python-3.7%2B-blue)](https://www.python.org/downloads/)  
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)  
[![Build Status](https://img.shields.io/badge/build-passing-brightgreen)](#)

A comprehensive, modular penetration testing framework designed for **authorized Windows security assessments**, cybersecurity research, and education.

---

## ⚡ Quick Start

### 📥 Installation (3 steps)

```bash
# 1) Install system dependencies (Debian / Kali)
sudo apt update && sudo apt install -y python3 python3-pip nmap samba-client

# 2) Clone repository
git clone https://github.com/cybersword1001/windows-penetration-testing-tool.git
cd windows-penetration-testing-tool

# 3) Create venv (recommended) and install Python deps
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

> **Important:** On Kali/Debian you may see PEP 668 warnings. Use a virtual environment (`venv`) or run `pip install --break-system-packages -r requirements.txt` only if you understand the risks.

---

## ▶️ Run the Tool

```bash
# Show banner + help
python3 main.py --help

# Scan a single host (safe, no exploitation)
python3 main.py -t 192.168.1.1 --scan-only -v

# Full assessment with simulated exploits (safe-mode)
python3 main.py -t 192.168.1.100 --exploit --post-exploit -v -o my_assessment
```

---

## 🛡️ Features

- 🔎 **Automated Reconnaissance** — host discovery, port & service enumeration  
- ⚠️ **Vulnerability Detection** — SMB checks, common Windows CVEs, weak configs  
- 💥 **Exploit Simulation** — safe-mode exploit flows for learning and demos  
- 🔐 **Post-Exploitation Checks** — privilege escalation, persistence checks  
- 📄 **Multi-format Reporting** — HTML (interactive), PDF, DOCX, JSON, Markdown  
- 📊 **Charts & Risk Scoring** — graphs for open ports and CVSS-like scoring  
- 🧩 **Modular Architecture** — easy to add new modules / scanners  
- 🎨 **Professional Startup Banner** — shows version, host, modules loaded

---

## 📘 Usage Examples

### 1) Scan only (safe)
```bash
python3 main.py -t 192.168.1.100 --scan-only -v
```

**Sample output**
```
[+] Scanning target: 192.168.1.100
[+] Found 5 open ports
[+] Services: SMB, RDP, HTTP
[+] Report saved to: reports/pentest_report_2025-11-26_104103.html
```

### 2) Full assessment (scan + simulated exploit)
```bash
python3 main.py -t 192.168.1.100 --exploit --post-exploit -v -o my_assessment
```

### 3) Network range scan
```bash
python3 main.py -t 192.168.1.0/24 --scan-only -v
```

### 4) Version check
```bash
python3 main.py --version
# Output: VulnScan Pentest Pro v0
```

---

## ⚙️ Configuration

### Default config — `config/default.json`
```json
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
    "formats": ["html", "pdf", "docx", "json", "markdown"],
    "detailed_logs": true
  }
}
```

**Use a custom config**
```bash
cp config/default.json config/custom.json
# edit config/custom.json
python3 main.py -t 192.168.1.100 -c config/custom.json
```

---

## 📂 Project Structure

```
windows-penetration-testing-tool/
├── main.py                 # Entry point (banner + CLI)
├── version.py              # Version metadata
├── requirements.txt        # Python dependencies
├── modules/                # Core scanning / exploit modules
│   ├── scanner.py
│   ├── vulnerability_detector.py
│   ├── exploiter.py
│   ├── post_exploit.py
│   └── reporter.py
├── utils/                  # Utility modules
│   ├── logger.py
│   ├── config.py
│   └── report_generator.py # Advanced report generator (HTML/PDF/DOCX)
├── config/
│   └── default.json
├── reports/                # Generated reports (html, pdf, docx, json)
├── docs/
│   ├── quickstart.md
│   └── usage.md
├── examples/
│   └── example_run.txt
└── .github/workflows/
    └── basic-check.yml
```

---

## 🤝 Contributing

Contributions are welcome!

**How to contribute**
1. Open an issue describing the bug or feature.  
2. Fork the repo and create a branch:
```bash
git checkout -b feature/my-feature
```
3. Make changes following PEP 8.  
4. Run `python3 test_installation.py` (if present).  
5. Commit & push, then open a PR.

**Commit style examples**
- `feat: add new scanner module`
- `fix: resolve CLI parsing bug`
- `docs: update README and usage examples`

---

## 📄 License

This project is licensed under the **MIT License**. See the `LICENSE` file for details.

---

## 👤 Author

**Created by:** [CYBERSWORD1001](https://github.com/cybersword1001)  
A security researcher focused on Windows security and open-source tooling.

---

## ⚖️ Legal Disclaimer

This tool is intended **ONLY** for authorized penetration testing, education, and research.

- ⚠ Unauthorized access is illegal.  
- ✔ Obtain written permission before testing.  
- ❌ The author is not responsible for misuse.

---

## 🧯 Safety Guidelines

- ✅ Test in your own lab or environment.  
- ✅ Begin with `--scan-only`.  
- ✅ Keep `safe_mode` enabled during tests.  
- ❌ Do not run exploits on systems without permission.

---

## 🛠 Troubleshooting

- **pip / modules errors**
```bash
source venv/bin/activate
pip3 install --upgrade -r requirements.txt
```

- **Permission denied**
```bash
chmod +x main.py
sudo chown -R $USER:$USER .
```

- **Nmap missing**
```bash
sudo apt install nmap
```

- **No hosts found**
```bash
python3 main.py -t 127.0.0.1 --scan-only -v
```

- **Line endings warning (LF/CRLF)**
```bash
git config core.autocrlf false
git add --renormalize .
git commit -m "fix: normalize line endings"
```

---

## 💬 Support

- 📘 Quick help → `docs/quickstart.md`  
- 📙 Detailed guide → `docs/usage.md`  
- 🐞 Bugs → Open a GitHub issue  
- 💬 Questions → Use GitHub Discussions

---

If you want, I can:
- generate `README.md` as a file and push it for you,  
- create `docs/quickstart.md` and `docs/usage.md` content, or  
- produce a demo GIF or screenshot for the README.

Tell me which one I should do next.
