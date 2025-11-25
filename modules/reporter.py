"""
Report Generation Module
Generates comprehensive penetration testing reports
"""

import json
import html
from datetime import datetime
from pathlib import Path
from utils.logger import get_logger

class ReportGenerator:
    def __init__(self, output_dir):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        self.logger = get_logger(__name__)
    
    def generate_report(self, results):
        """Generate comprehensive report in multiple formats"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # Generate JSON report
        json_file = self.output_dir / f"pentest_report_{timestamp}.json"
        self._generate_json_report(results, json_file)
        
        # Generate HTML report
        html_file = self.output_dir / f"pentest_report_{timestamp}.html"
        self._generate_html_report(results, html_file)
        
        # Generate Markdown report
        md_file = self.output_dir / f"pentest_report_{timestamp}.md"
        self._generate_markdown_report(results, md_file)
        
        self.logger.info(f"Reports generated in {self.output_dir}")
        return {
            'json': str(json_file),
            'html': str(html_file),
            'markdown': str(md_file)
        }
    
    def _generate_json_report(self, results, filename):
        """Generate JSON report"""
        with open(filename, 'w') as f:
            json.dump(results, f, indent=2, default=str)
    
    def _generate_html_report(self, results, filename):
        """Generate HTML report"""
        html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Windows Penetration Test Report</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 40px; }}
        .header {{ background-color: #2c3e50; color: white; padding: 20px; text-align: center; }}
        .section {{ margin: 20px 0; }}
        .vulnerability {{ border: 1px solid #ddd; margin: 10px 0; padding: 15px; }}
        .critical {{ border-left: 5px solid #e74c3c; }}
        .high {{ border-left: 5px solid #f39c12; }}
        .medium {{ border-left: 5px solid #f1c40f; }}
        .low {{ border-left: 5px solid #27ae60; }}
        .info {{ border-left: 5px solid #3498db; }}
        table {{ border-collapse: collapse; width: 100%; }}
        th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
        th {{ background-color: #f2f2f2; }}
    </style>
</head>
<body>
    <div class="header">
        <h1>Windows Penetration Test Report</h1>
        <p>Generated on {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</p>
        <p>Target: {html.escape(results['target'])}</p>
    </div>
    
    <div class="section">
        <h2>Executive Summary</h2>
        <p>This report contains the results of a penetration test conducted on the target system(s). 
        The assessment identified {len(results.get('vulnerabilities', []))} vulnerabilities across 
        {len(results.get('scan_results', {}).get('host_discovery', []))} discovered hosts.</p>
    </div>
    
    <div class="section">
        <h2>Discovered Hosts</h2>
        <table>
            <tr><th>Host</th><th>Open Ports</th><th>Services</th></tr>
            {self._generate_host_table(results)}
        </table>
    </div>
    
    <div class="section">
        <h2>Vulnerabilities</h2>
        {self._generate_vulnerability_section(results.get('vulnerabilities', []))}
    </div>
    
    <div class="section">
        <h2>Exploitation Results</h2>
        {self._generate_exploitation_section(results.get('exploits', []))}
    </div>
    
    <div class="section">
        <h2>Post-Exploitation Results</h2>
        {self._generate_post_exploit_section(results.get('post_exploit', []))}
    </div>
    
    <div class="section">
        <h2>Recommendations</h2>
        <ul>
            <li>Patch all identified vulnerabilities immediately</li>
            <li>Implement network segmentation</li>
            <li>Enable SMB signing on all systems</li>
            <li>Disable SMBv1 protocol</li>
            <li>Implement strong password policies</li>
            <li>Enable Windows Defender or equivalent antivirus</li>
            <li>Regular security updates and patch management</li>
        </ul>
    </div>
</body>
</html>
        """
        
        with open(filename, 'w') as f:
            f.write(html_content)
    
    def _generate_markdown_report(self, results, filename):
        """Generate Markdown report"""
        md_content = f"""# Windows Penetration Test Report

**Generated:** {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}  
**Target:** {results['target']}

## Executive Summary

This report contains the results of a penetration test conducted on the target system(s). The assessment identified {len(results.get('vulnerabilities', []))} vulnerabilities across {len(results.get('scan_results', {}).get('host_discovery', []))} discovered hosts.

## Discovered Hosts

{self._generate_host_markdown(results)}

## Vulnerabilities

{self._generate_vulnerability_markdown(results.get('vulnerabilities', []))}

## Exploitation Results

{self._generate_exploitation_markdown(results.get('exploits', []))}

## Post-Exploitation Results

{self._generate_post_exploit_markdown(results.get('post_exploit', []))}

## Recommendations

- Patch all identified vulnerabilities immediately
- Implement network segmentation
- Enable SMB signing on all systems
- Disable SMBv1 protocol
- Implement strong password policies
- Enable Windows Defender or equivalent antivirus
- Regular security updates and patch management
"""
        
        with open(filename, 'w') as f:
            f.write(md_content)
    
    def _generate_host_table(self, results):
        """Generate HTML table for discovered hosts"""
        html_rows = ""
        scan_results = results.get('scan_results', {})
        
        for host in scan_results.get('host_discovery', []):
            ports = scan_results.get('port_scan', {}).get(host, [])
            services = scan_results.get('service_enumeration', {}).get(host, {})
            
            ports_str = ', '.join(map(str, ports))
            services_str = ', '.join([f"{port}:{info.get('service', 'Unknown')}" 
                                    for port, info in services.items()])
            
            html_rows += f"<tr><td>{html.escape(host)}</td><td>{html.escape(ports_str)}</td><td>{html.escape(services_str)}</td></tr>"
        
        return html_rows
    
    def _generate_vulnerability_section(self, vulnerabilities):
        """Generate HTML for vulnerabilities"""
        html_content = ""
        
        for vuln in vulnerabilities:
            severity_class = vuln.get('severity', 'info').lower()
            html_content += f"""
            <div class="vulnerability {severity_class}">
                <h3>{html.escape(vuln.get('vulnerability', 'Unknown'))}</h3>
                <p><strong>Host:</strong> {html.escape(vuln.get('host', 'Unknown'))}</p>
                <p><strong>Severity:</strong> {html.escape(vuln.get('severity', 'Unknown'))}</p>
                <p><strong>Port:</strong> {vuln.get('port', 'N/A')}</p>
                <p><strong>CVE:</strong> {html.escape(vuln.get('cve', 'N/A'))}</p>
                <p><strong>Description:</strong> {html.escape(vuln.get('description', 'No description'))}</p>
            </div>
            """
        
        return html_content
    
    def _generate_exploitation_section(self, exploits):
        """Generate HTML for exploitation results"""
        if not exploits:
            return "<p>No exploitation attempts were made.</p>"
        
        html_content = ""
        for exploit in exploits:
            success_class = "high" if exploit.get('success') else "info"
            html_content += f"""
            <div class="vulnerability {success_class}">
                <h3>{html.escape(exploit.get('vulnerability', 'Unknown'))}</h3>
                <p><strong>Host:</strong> {html.escape(exploit.get('host', 'Unknown'))}</p>
                <p><strong>Method:</strong> {html.escape(exploit.get('method', 'Unknown'))}</p>
                <p><strong>Success:</strong> {exploit.get('success', False)}</p>
                <p><strong>Note:</strong> {html.escape(exploit.get('note', 'No additional notes'))}</p>
            </div>
            """
        
        return html_content
    
    def _generate_post_exploit_section(self, post_exploits):
        """Generate HTML for post-exploitation results"""
        if not post_exploits:
            return "<p>No post-exploitation activities were performed.</p>"
        
        html_content = ""
        for result in post_exploits:
            html_content += f"""
            <div class="vulnerability info">
                <h3>Post-Exploitation: {html.escape(result.get('host', 'Unknown'))}</h3>
                <p><strong>Exploit Method:</strong> {html.escape(result.get('exploit_method', 'Unknown'))}</p>
                <p><strong>Privilege Escalation Checks:</strong> {len(result.get('privilege_escalation', []))}</p>
                <p><strong>Credential Dumps:</strong> {len(result.get('credentials', []))}</p>
                <p><strong>Lateral Movement:</strong> {len(result.get('lateral_movement', []))}</p>
                <p><strong>Persistence:</strong> {len(result.get('persistence', []))}</p>
            </div>
            """
        
        return html_content
    
    def _generate_host_markdown(self, results):
        """Generate Markdown for discovered hosts"""
        md_content = "| Host | Open Ports | Services |\n|------|------------|----------|\n"
        scan_results = results.get('scan_results', {})
        
        for host in scan_results.get('host_discovery', []):
            ports = scan_results.get('port_scan', {}).get(host, [])
            services = scan_results.get('service_enumeration', {}).get(host, {})
            
            ports_str = ', '.join(map(str, ports))
            services_str = ', '.join([f"{port}:{info.get('service', 'Unknown')}" 
                                    for port, info in services.items()])
            
            md_content += f"| {host} | {ports_str} | {services_str} |\n"
        
        return md_content
    
    def _generate_vulnerability_markdown(self, vulnerabilities):
        """Generate Markdown for vulnerabilities"""
        if not vulnerabilities:
            return "No vulnerabilities identified.\n"
        
        md_content = ""
        for vuln in vulnerabilities:
            md_content += f"""
### {vuln.get('vulnerability', 'Unknown')}

- **Host:** {vuln.get('host', 'Unknown')}
- **Severity:** {vuln.get('severity', 'Unknown')}
- **Port:** {vuln.get('port', 'N/A')}
- **CVE:** {vuln.get('cve', 'N/A')}
- **Description:** {vuln.get('description', 'No description')}

"""
        
        return md_content
    
    def _generate_exploitation_markdown(self, exploits):
        """Generate Markdown for exploitation results"""
        if not exploits:
            return "No exploitation attempts were made.\n"
        
        md_content = ""
        for exploit in exploits:
            md_content += f"""
### {exploit.get('vulnerability', 'Unknown')}

- **Host:** {exploit.get('host', 'Unknown')}
- **Method:** {exploit.get('method', 'Unknown')}
- **Success:** {exploit.get('success', False)}
- **Note:** {exploit.get('note', 'No additional notes')}

"""
        
        return md_content
    
    def _generate_post_exploit_markdown(self, post_exploits):
        """Generate Markdown for post-exploitation results"""
        if not post_exploits:
            return "No post-exploitation activities were performed.\n"
        
        md_content = ""
        for result in post_exploits:
            md_content += f"""
### Post-Exploitation: {result.get('host', 'Unknown')}

- **Exploit Method:** {result.get('exploit_method', 'Unknown')}
- **Privilege Escalation Checks:** {len(result.get('privilege_escalation', []))}
- **Credential Dumps:** {len(result.get('credentials', []))}
- **Lateral Movement:** {len(result.get('lateral_movement', []))}
- **Persistence:** {len(result.get('persistence', []))}

"""
        
        return md_content
