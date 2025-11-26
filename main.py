#!/usr/bin/env python3
"""
Windows Penetration Testing Tool
A modular framework for authorized Windows security testing
"""

# ========================= BANNER SECTION =========================
import os
import platform
from datetime import datetime

try:
    from pyfiglet import figlet_format
    from colorama import init as colorama_init, Fore, Style
    colorama_init(autoreset=True)
except ImportError:
    def figlet_format(t, font="standard"):
        return t
    class Fore:
        CYAN = ""
        GREEN = ""
        YELLOW = ""
        MAGENTA = ""
        RED = ""
        RESET = ""
    class Style:
        RESET_ALL = ""

def count_files(path):
    """Count total files in a directory recursively"""
    total = 0
    if os.path.exists(path):
        for _, _, files in os.walk(path):
            total += len(files)
    return total

def show_banner():
    """Display a professional startup banner with system info"""
    title = figlet_format("VulnScan Pentest Pro", font="slant")
    mascot = r"""
        ▄████▄   ██▀███   ▄▄▄       ███▄    █ 
       ▒██▀ ▀█  ▓██ ▒ ██▒▒████▄     ██ ▀█   █ 
       ▒▓█    ▄ ▓██ ░▄█ ▒▒██  ▀█▄  ▓██  ▀█ ██▒
       ▒▓▓▄ ▄██▒▒██▀▀█▄  ░██▄▄▄▄██ ▓██▒  ▐▌██▒
       ▒ ▓███▀ ░░██▓ ▒██▒ ▓█   ▓██▒▒██░   ▓██░
       ░ ░▒ ▒  ░░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░ ▒░   ▒ ▒ 
         ░  ▒     ░▒ ░ ▒░  ▒   ▒▒ ░░ ░░   ░ ▒░
       ░          ░░   ░   ░   ▒      ░   ░ ░ 
       ░ ░         ░           ░  ░         ░ 
       ░
    """
    modules = count_files("modules")
    utils = count_files("utils")
    configs = count_files("config")
    print(Fore.RED + title + Style.RESET_ALL)
    print(mascot)
    print("=" * 75)
    print(f"{Fore.CYAN}[+] Version: v0  |  Host: {platform.node()}  |  Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}{Style.RESET_ALL}")
    print(f"{Fore.GREEN}[+] Modules Loaded: {modules}   |   Utils: {utils}   |   Configs: {configs}{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}[+] Features: Recon  |  Scanning  |  Vulnerability Detection  |  Reporting{Style.RESET_ALL}")
    print(f"{Fore.MAGENTA}[+] Created by: CYBERSWORD1001{Style.RESET_ALL}")
    print("=" * 75)
    print()

# ========================= END BANNER SECTION =========================

import argparse
import sys
import json
from pathlib import Path

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from version import __version__, __author__

try:
    from modules.scanner import NetworkScanner
    from modules.vulnerability_detector import VulnerabilityDetector
    from modules.exploiter import ExploitManager
    from modules.post_exploit import PostExploitManager
    from modules.reporter import ReportGenerator
    from utils.report_generator import generate_reports
    from utils.logger import setup_logger
    from utils.config import Config
except ImportError as e:
    print(f"❌ Import Error: {e}")
    print("Please make sure all required files are present and run: pip3 install -r requirements.txt")
    sys.exit(1)

def check_requirements():
    """Check if basic Python requirements are met"""
    try:
        import socket
        import subprocess
        import threading
        import concurrent.futures
        return True
    except ImportError as e:
        print(f"❌ Missing required Python module: {e}")
        return False

def main():
    """Main entry point for the penetration testing tool"""
    show_banner()
    
    # Check basic requirements
    if not check_requirements():
        print("Please install missing dependencies and try again.")
        sys.exit(1)
    
    parser = argparse.ArgumentParser(
        description='Windows Penetration Testing Tool - Authorized testing only',
        epilog='Example: python3 main.py -t 192.168.1.100 --scan-only -v'
    )
    parser.add_argument('-t', '--target', required=True,
                        help='Target IP or range (e.g., 192.168.1.1 or 192.168.1.0/24)')
    parser.add_argument('-c', '--config', default='config/default.json',
                        help='Configuration file (default: config/default.json)')
    parser.add_argument('-o', '--output', default='reports',
                        help='Output directory for reports (default: reports)')
    parser.add_argument('-v', '--verbose', action='store_true',
                        help='Enable verbose output')
    parser.add_argument('--scan-only', action='store_true',
                        help='Perform network scanning only')
    parser.add_argument('--exploit', action='store_true',
                        help='Enable exploitation modules (simulation mode)')
    parser.add_argument('--post-exploit', action='store_true',
                        help='Enable post-exploitation modules')
    parser.add_argument('--version', action='version',
                        version=f'%(prog)s {__version__}')
    
    args = parser.parse_args()
    
    # Create necessary directories
    Path(args.output).mkdir(exist_ok=True)
    Path('logs').mkdir(exist_ok=True)
    Path('config').mkdir(exist_ok=True)
    
    try:
        # Setup logging
        logger = setup_logger(verbose=args.verbose)
        logger.info("Starting Windows Penetration Testing Tool")
        
        # Load configuration
        config = Config(args.config)
        
        # Initialize modules
        scanner = NetworkScanner(config)
        vuln_detector = VulnerabilityDetector(config)
        exploit_manager = ExploitManager(config)
        post_exploit_manager = PostExploitManager(config)
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        report_basename = f"pentest_report_{timestamp}"
        
        results = {
            'target': args.target,
            'scan_results': {},
            'vulnerabilities': [],
            'exploits': [],
            'post_exploit': []
        }
        
        # Phase 1: Reconnaissance and Scanning
        logger.info(f"Starting reconnaissance on target: {args.target}")
        scan_results = scanner.scan_target(args.target)
        results['scan_results'] = scan_results
        
        if args.scan_only:
            logger.info("Scan-only mode. Generating advanced reports...")
            findings = _convert_to_findings(scan_results)
            report_files = generate_reports(findings, f"{args.output}/{report_basename}")
            print(f"\n✅ Scan completed! Reports saved in: {args.output}/")
            for format_type, file_path in report_files.items():
                print(f"   {format_type.upper()}: {file_path}")
            print("Thanks for using VulnScan Pentest Pro. Stay ethical!\n")
            return
        
        # Phase 2: Vulnerability Detection
        logger.info("Analyzing for vulnerabilities...")
        vulnerabilities = vuln_detector.detect_vulnerabilities(scan_results)
        results['vulnerabilities'] = vulnerabilities
        
        # Phase 3: Exploitation (if enabled)
        if args.exploit and vulnerabilities:
            logger.info("Starting exploitation phase...")
            exploit_results = exploit_manager.exploit_vulnerabilities(vulnerabilities)
            results['exploits'] = exploit_results
            
            # Phase 4: Post-Exploitation (if enabled and exploits successful)
            if args.post_exploit and any(e.get('success', False) for e in exploit_results):
                logger.info("Starting post-exploitation phase...")
                post_results = post_exploit_manager.run_post_exploit(exploit_results)
                results['post_exploit'] = post_results
        
        logger.info("Generating advanced reports with risk analysis...")
        findings = _convert_vulnerabilities_to_findings(vulnerabilities)
        report_files = generate_reports(findings, f"{args.output}/{report_basename}")
        
        print(f"\n✅ Assessment completed successfully!")
        print(f"📊 Reports generated:")
        for format_type, file_path in report_files.items():
            print(f"   {format_type.upper()}: {file_path}")
        
        print("\nThanks for using VulnScan Pentest Pro. Stay ethical!\n")
        
    except KeyboardInterrupt:
        print("\n⚠️  Operation interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ An error occurred: {str(e)}")
        if args.verbose:
            import traceback
            traceback.print_exc()
        sys.exit(1)

def _convert_to_findings(scan_results):
    """Convert scan results to findings format for report generator"""
    findings = []
    
    # scan_results is a dict with keys: host_discovery, port_scan, service_enumeration, etc.
    try:
        port_scan = scan_results.get('port_scan', {})
        service_enum = scan_results.get('service_enumeration', {})
        
        # Iterate through each host and its ports
        for host, ports in port_scan.items():
            services = service_enum.get(host, {})
            
            # Create a finding for each open port
            for port in ports:
                service_info = services.get(port, {})
                finding = {
                    'host': host,
                    'port': port,
                    'service': service_info.get('service', 'Unknown'),
                    'severity': 'info',  # Default severity for discovered services
                    'vulnerability': f'Open {service_info.get("service", "Unknown")} Port',
                    'note': service_info.get('banner', 'Service detected'),
                    'exploitability': 0.3,
                    'impact': 0.3
                }
                findings.append(finding)
    except Exception as e:
        print(f"Warning: Error converting scan results: {e}")
    
    return findings

def _convert_vulnerabilities_to_findings(vulnerabilities):
    """Convert vulnerability data to findings format for report generator"""
    findings = []
    for vuln in vulnerabilities:
        finding = {
            'host': vuln.get('host', 'Unknown'),
            'port': vuln.get('port', 'N/A'),
            'service': vuln.get('service', 'Unknown'),
            'severity': vuln.get('severity', 'info'),
            'vulnerability': vuln.get('vulnerability', 'Unknown'),
            'note': vuln.get('description', 'No description'),
            'exploitability': vuln.get('exploitability', 0.5),
            'impact': vuln.get('impact', 0.5)
        }
        findings.append(finding)
    return findings

if __name__ == "__main__":
    main()
