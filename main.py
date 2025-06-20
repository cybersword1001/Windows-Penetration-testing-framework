#!/usr/bin/env python3
"""
Windows Penetration Testing Tool
A modular framework for authorized Windows security testing
"""

import argparse
import sys
import json
import os
from pathlib import Path

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from modules.scanner import NetworkScanner
    from modules.vulnerability_detector import VulnerabilityDetector
    from modules.exploiter import ExploitManager
    from modules.post_exploit import PostExploitManager
    from modules.reporter import ReportGenerator
    from utils.logger import setup_logger
    from utils.config import Config
except ImportError as e:
    print(f"❌ Import Error: {e}")
    print("Please make sure all required files are present and run: pip3 install -r requirements.txt")
    sys.exit(1)

def banner():
    print("""
╔══════════════════════════════════════════════════════════════╗
║                Windows PenTest Tool v1.0                    ║
║              For Authorized Testing Only                     ║
╚══════════════════════════════════════════════════════════════╝
    """)

def check_requirements():
    """Check if basic requirements are met"""
    try:
        import socket
        import subprocess
        import threading
        import concurrent.futures
        print("✅ Basic Python modules available")
        return True
    except ImportError as e:
        print(f"❌ Missing required Python module: {e}")
        return False

def main():
    banner()
    
    # Check basic requirements
    if not check_requirements():
        print("Please install missing dependencies and try again.")
        sys.exit(1)
    
    parser = argparse.ArgumentParser(description='Windows Penetration Testing Tool')
    parser.add_argument('-t', '--target', required=True, help='Target IP or range (e.g., 192.168.1.1 or 192.168.1.0/24)')
    parser.add_argument('-c', '--config', default='config/default.json', help='Configuration file')
    parser.add_argument('-o', '--output', default='reports', help='Output directory for reports')
    parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    parser.add_argument('--scan-only', action='store_true', help='Perform scanning only')
    parser.add_argument('--exploit', action='store_true', help='Enable exploitation modules')
    parser.add_argument('--post-exploit', action='store_true', help='Enable post-exploitation modules')
    
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
        reporter = ReportGenerator(args.output)
        
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
            logger.info("Scan-only mode. Generating report...")
            reporter.generate_report(results)
            print(f"\n✅ Scan completed! Reports saved in: {args.output}/")
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
        
        # Generate comprehensive report
        logger.info("Generating final report...")
        report_files = reporter.generate_report(results)
        
        print(f"\n✅ Assessment completed successfully!")
        print(f"📊 Reports generated:")
        for format_type, file_path in report_files.items():
            print(f"   {format_type.upper()}: {file_path}")
        
    except KeyboardInterrupt:
        print("\n⚠️  Operation interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ An error occurred: {str(e)}")
        if args.verbose:
            import traceback
            traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()
