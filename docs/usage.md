# Detailed Usage Guide

## Command-Line Arguments

### Required Arguments
- `-t, --target`: Target IP address or CIDR range
  - Single host: `192.168.1.100`
  - Network range: `192.168.1.0/24`

### Optional Arguments
- `-c, --config`: Custom configuration file (default: `config/default.json`)
- `-o, --output`: Output directory for reports (default: `reports`)
- `-v, --verbose`: Enable detailed logging
- `--scan-only`: Perform only network scanning (recommended for first run)
- `--exploit`: Enable exploitation modules (simulation mode)
- `--post-exploit`: Enable post-exploitation modules
- `--version`: Display version and exit
- `--help`: Display help message

## Execution Phases

### Phase 1: Network Scanning
- Host discovery
- Port scanning
- Service enumeration
- Banner grabbing

### Phase 2: Vulnerability Detection
- Identifies common Windows vulnerabilities
- Cross-references with CVE databases
- Severity assessment

### Phase 3: Exploitation (Optional)
- Simulated exploitation (safe mode)
- Generates proof-of-concept output

### Phase 4: Post-Exploitation (Optional)
- Privilege escalation checks
- Lateral movement possibilities
- Persistence mechanisms

## Output Reports

Generated in `reports/` directory:
- **HTML Report**: Full visual report with charts
- **JSON Report**: Machine-readable format
- **Markdown Report**: Text-based summary

Example: `pentest_report_20240115_103025.html`

## Log Files

Located in `logs/` directory:
- Contains detailed execution logs
- Useful for troubleshooting
- Search for errors: `grep -i error logs/*.log`

## Safety Considerations

1. Always get written authorization before testing
2. Start with `--scan-only` mode
3. Test on your own systems first
4. Keep detailed records
5. Follow responsible disclosure
