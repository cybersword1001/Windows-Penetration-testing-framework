# 🚀 VulnScan Pentest Pro  
[![Python 3.7+](https://img.shields.io/badge/python-3.7%2B-blue)](https://www.python.org/downloads/)  
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)  
[![Build Status](https://img.shields.io/badge/build-passing-brightgreen)](#)

A comprehensive and modular penetration testing framework designed for **authorized Windows security assessments**, cybersecurity research, and ethical hacking education.

---

# ⚡ Quick Start

## 📥 Installation (3 Steps)

```bash
# 1. Install system dependencies
sudo apt update && sudo apt install -y python3 python3-pip nmap samba-client

# 2. Clone the repository
git clone https://github.com/cybersword1001/windows-penetration-testing-tool.git
cd windows-penetrration-testing-tool

# 3. Install Python dependencies
pip3 install -r requirements.txt
```

---

## ▶️ Running the Tool

```bash
# Show banner + help menu
python3 main.py --help

# Basic scan
python3 main.py -t 192.168.1.1 --scan-only -v

# Full assessment (recon + vulnerabilities + simulated exploit)
python3 main.py -t 192.168.1.100 --exploit --post-exploit -v
```

---

# 🛡️ Features

- 🔎 **Automated Recon** — Network scan, host discovery, service detection  
- ⚠️ **Vulnerability Detection** — SMB flaws, weak configs, common Windows CVEs  
- 💥 **Exploit Simulation** — Safe-mode exploit framework for education  
- 🎯 **Post-Exploitation Checks** — Permissions, misconfigurations, persistence  
- 📑 **Report Generation** — HTML, JSON, and Markdown formats  
- 🧩 **Modular Architecture** — Easy extension through modules  
- 🎨 **Professional Banner** — System info + module count on startup  

---

# 📘 Usage Examples

### 1️⃣ **Scan Only (Safe Mode)**
```bash
python3 main.py -t 192.168.1.100 --scan-only -v
```

**Example Output**
```
[+] Scanning target: 192.168.1.100  
[+] Found 5 open ports  
[+] Services: SMB, RDP, HTTP  
[+] Report saved to: reports/pentest_report_*.html  
```

---

### 2️⃣ **Full Assessment (Scan + Exploit Simulation)**
```bash
python3 main.py -t 192.168.1.100 --exploit --post-exploit -v -o my_assessment
```

---

### 3️⃣ **Scan Entire Network Range**
```bash
python3 main.py -t 192.168.1.0/24 --scan-only -v
```

---

### 4️⃣ **Check Tool Version**
```bash
python3 main.py --version
# VulnScan Pentest Pro v0
```

---

# ⚙️ Configuration

## 📁 Default Config (`config/default.json`)
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
    "formats": ["html", "json", "markdown"],
    "detailed_logs": true
  }
}
```

### ✨ Custom Config Example:
```bash
cp config/default.json config/custom.json
python3 main.py -t 192.168.1.100 -c config/custom.json
```

---

# 📂 Project Structure

```
windows-penetration-testing-tool/
├── main.py                 # Entry point (banner + CLI)
├── version.py              # Version metadata
├── requirements.txt        # Python dependencies

├── modules/                # Core scanning/exploitation modules
│   ├── scanner.py
│   ├── vulnerability_detector.py
│   ├── exploiter.py
│   ├── post_exploit.py
│   └── reporter.py

├── utils/                  # Utility modules
│   ├── logger.py
│   └── config.py

├── config/                 # Configuration
│   └── default.json

├── docs/                   # Documentation
│   ├── quickstart.md
│   └── usage.md

├── examples/
│   └── example_run.txt

└── .github/workflows/
    └── basic-check.yml     # CI pipeline
```

---

# 🤝 Contributing

We welcome contributions from the cybersecurity community.

### ✔ How to Contribute
1. Open an issue describing your idea or bug  
2. Fork the repository  
3. Create a branch:
   ```bash
   git checkout -b feature/my-feature
   ```
4. Make changes following PEP-8  
5. Commit & push:
   ```bash
   git commit -m "feat: add new feature"
   git push origin feature/my-feature
   ```
6. Submit a Pull Request

---

# 📄 License

Licensed under the **MIT License**.  
See the `LICENSE` file for details.

---

# 👤 Author

### **Created by:**  
🔗 **[CYBERSWORD1001](https://github.com/cybersword1001)**  

Cybersecurity researcher specializing in Windows security and penetration testing tools.

---

# ⚖️ Legal Disclaimer

This tool is intended **ONLY** for:

- Authorized penetration testing  
- Cybersecurity education  
- Ethical hacking research  

❌ Unauthorized access to systems is illegal  
❌ You are fully responsible for misuse  
✔ Always obtain written permission  

---

# 🧯 Safety Guidelines

- ✔ Test in a controlled lab environment  
- ✔ Begin with `--scan-only`  
- ✔ Safe Mode is enabled by default  
- ❌ Do NOT scan unknown networks  
- ❌ Avoid production systems without approval  

---

# 🛠 Troubleshooting

### ❗ Module errors / Python issues  
```bash
pip3 install --upgrade -r requirements.txt
```

### ❗ Permission denied  
```bash
chmod +x main.py
sudo chown -R $USER:$USER .
```

### ❗ Nmap missing  
```bash
sudo apt install nmap
```

### ❗ No hosts found  
```bash
python3 main.py -t 127.0.0.1 --scan-only -v
```

---

# 💬 Support

📘 Quick Help → `docs/quickstart.md`  
📙 Full Guide → `docs/usage.md`  
🐞 Bugs → GitHub Issues  
💬 Questions → Discussions  
