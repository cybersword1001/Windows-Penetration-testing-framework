# Windows Penetration Toolkit — Landing & Demo

[![CI](https://github.com/yourusername/windows-penetration-toolkit/actions/workflows/ci.yml/badge.svg)](https://github.com/yourusername/windows-penetration-toolkit/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A production-ready web application presenting a safe, simulated environment for learning Windows penetration testing workflows. This project allows users to visualize recon, exploitation, and post-exploitation steps without risking actual infrastructure.

**⚠️ EDUCATIONAL USE ONLY. NO REAL EXPLOITS.**

## Features

- **Interactive Simulation Demo**: Visualizes attack chains without executing real code.
- **Safe Architecture**: All "exploits" are mocked JSON data or pre-recorded animations.
- **Legal & Compliance**: Built-in responsible disclosure and authorization templates.
- **Modern Tech Stack**: React 18, Vite, Tailwind CSS, Framer Motion.

## Project Structure

- `/src`: React application source code (Vite).
- `/python-tool`: The legacy Python CLI tool (preserved from previous version).
- `/public`: Static assets (simulated downloads, media).

## Quick Start (Web App)

This runs the visual landing page and demo interface.

1.  **Clone the repository:**
    \`\`\`bash
    git clone https://github.com/yourusername/windows-penetration-toolkit.git
    cd windows-penetration-toolkit
    \`\`\`

2.  **Install dependencies:**
    \`\`\`bash
    npm install
    \`\`\`

3.  **Run local development server:**
    \`\`\`bash
    npm run dev
    \`\`\`

4.  **Build for production:**
    \`\`\`bash
    npm run build
    \`\`\`

## Quick Start (Python CLI Tool)

This runs the actual penetration testing script.

1.  **Navigate to the tool directory:**
    \`\`\`bash
    cd python-tool
    \`\`\`

2.  **Install Python dependencies:**
    \`\`\`bash
    pip install -r requirements.txt
    \`\`\`

3.  **Run the tool:**
    \`\`\`bash
    # Example: Scan a local device
    python main.py -t 127.0.0.1 --scan-only -v
    \`\`\`

    See [python-tool/README.md](python-tool/README.md) for full documentation.

## Development Environment (VS Code)

**Yes, you can run this in VS Code.** Here is the best setup:

### 1. Running the Web App (Frontend)
*   **OS:** Any (Windows, macOS, Linux, Kali, Parrot).
*   **VS Code:** Open the root folder `windows-penetration-toolkit`.
*   **Terminal:** Open a terminal in VS Code (`Ctrl+` `) and run `npm run dev`.

### 2. Running the Python Tool (Backend)
*   **OS:** **Kali Linux or Parrot OS is highly recommended** because this tool relies on `nmap` and raw socket permissions.
*   **VS Code Setup:**
    *   **Option A (Best):** Run VS Code directly inside Kali/Parrot.
    *   **Option B (Windows + WSL):** Install WSL2 (Kali or Ubuntu), then use the "Remote - WSL" extension in VS Code to open the folder *inside* the Linux system.
*   **Terminal:** Open the terminal in VS Code, `cd python-tool`, and run `sudo python main.py ...` (Root permissions are often needed for network scanning).

## Deploy to Vercel

This project is configured for zero-config deployment on Vercel.

1.  Push your code to a GitHub repository.
2.  Import the project in Vercel.
3.  Framework Preset: **Vite**.
4.  Build Command: `npm run build`.
5.  Output Directory: `dist`.
6.  Deploy!

## Safety & Legal

This repository strictly adheres to safety guidelines:
*   **No Malware:** Contains no virus, worm, Trojan, or real exploit payloads.
*   **Simulated Only:** All "attacks" are visual simulations only.
*   **Authorization:** Users must download and sign the Authorization Template before using any pentesting methodology on real systems.

See [RESPONSIBLE_DISCLOSURE.md](RESPONSIBLE_DISCLOSURE.md) for our security policy.

## License

MIT License. See [LICENSE](LICENSE) file.
