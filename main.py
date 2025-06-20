#!/usr/bin/env python3
"""
Windows Penetration Testing Tool
A modular framework for authorized Windows security testing
"""

import argparse
import sys
import json
from pathlib import Path
from modules.scanner import NetworkScanner
from modules.vulnerability_detector import VulnerabilityDetector
from modules.exploiter import ExploitManager
from modules.post_exploit import PostExploitManager
from modules.reporter import ReportGenerator
from utils.logger import setup_logger
from utils.config import Config

def banner():
    print("""
╔══════════════════════════════════════════════════════════════╗
║                Windows PenTest Tool v1.0                    ║
║              For Authorized Testing Only                     ║
╚══════════════════════════════════════════════════════════════╝
    """)

def main():
    banner()
    
    parser = argparse.ArgumentParser(description='Windows Penetration Testing Tool')
    parser.add_argument('-t', '--target', required=True, help='Target IP or range (e.g., 192.168.1.1 or 192.168.1.0/24)')
    parser.add_argument('-c', '--config', default='config/default.json', help='Configuration file')
    parser.add_argument('-o', '--output', default='reports', help='Output directory for reports')
    parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    parser.add_argument('--scan-only', action='store_true', help='Perform scanning only')
    parser.add_argument('--exploit', action='store_true', help='Enable exploitation modules')
    parser.add_argument('--post-exploit', action='store_true', help='Enable post-exploitation modules')
    
    args = parser.parse_args()
    
    # Setup logging
    logger = setup_logger(verbose=args.verbose)
    
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
    
    try:
        # Phase 1: Reconnaissance and Scanning
        logger.info(f"Starting reconnaissance on target: {args.target}")
        scan_results = scanner.scan_target(args.target)
        results['scan_results'] = scan_results
        
        if args.scan_only:
            logger.info("Scan-only mode. Generating report...")
            reporter.generate_report(results)
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
            if args.post_exploit and any(e['success'] for e in exploit_results):
                logger.info("Starting post-exploitation phase...")
                post_results = post_exploit_manager.run_post_exploit(exploit_results)
                results['post_exploit'] = post_results
        
        # Generate comprehensive report
        logger.info("Generating final report...")
        reporter.generate_report(results)
        
    except KeyboardInterrupt:
        logger.info("Operation interrupted by user")
        sys.exit(1)
    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
