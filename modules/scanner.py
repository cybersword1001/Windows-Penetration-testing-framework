"""
Network Scanner Module
Handles reconnaissance and service enumeration
"""

import socket
import threading
import subprocess
import json
import platform
import ipaddress
from concurrent.futures import ThreadPoolExecutor
from utils.logger import get_logger

class NetworkScanner:
    def __init__(self, config):
        self.config = config
        self.logger = get_logger(__name__)
        self.common_ports = [21, 22, 23, 25, 53, 80, 110, 111, 135, 139, 143, 443, 445, 993, 995, 1723, 3306, 3389, 5432, 5900, 8080]
        
    def scan_target(self, target):
        """Main scanning function"""
        results = {
            'host_discovery': [],
            'port_scan': {},
            'service_enumeration': {},
            'smb_enumeration': {},
            'ldap_enumeration': {}
        }
        
        try:
            # Host discovery
            self.logger.info("Starting host discovery...")
            hosts = self._discover_hosts(target)
            results['host_discovery'] = hosts
            
            if not hosts:
                self.logger.warning("No live hosts discovered")
                return results
            
            # Port scanning for each discovered host
            for host in hosts:
                self.logger.info(f"Scanning ports on {host}")
                open_ports = self._port_scan(host)
                results['port_scan'][host] = open_ports
                
                if open_ports:
                    # Service enumeration
                    services = self._enumerate_services(host, open_ports)
                    results['service_enumeration'][host] = services
                    
                    # SMB enumeration if port 445 is open
                    if 445 in open_ports:
                        smb_info = self._enumerate_smb(host)
                        results['smb_enumeration'][host] = smb_info
                    
                    # LDAP enumeration if port 389 is open
                    if 389 in open_ports:
                        ldap_info = self._enumerate_ldap(host)
                        results['ldap_enumeration'][host] = ldap_info
                else:
                    self.logger.info(f"No open ports found on {host}")
            
        except Exception as e:
            self.logger.error(f"Error during scanning: {str(e)}")
        
        return results
    
    def _discover_hosts(self, target):
        """Discover live hosts in the target range"""
        hosts = []
        
        try:
            if '/' in target:  # CIDR notation
                self.logger.info(f"Discovering hosts in network: {target}")
                network = ipaddress.IPv4Network(target, strict=False)
                
                def ping_host(ip):
                    try:
                        # Determine ping parameters based on OS
                        if platform.system().lower() == 'windows':
                            cmd = ['ping', '-n', '1', '-w', '1000', str(ip)]
                        else:
                            cmd = ['ping', '-c', '1', '-W', '1', str(ip)]
                        
                        result = subprocess.run(cmd, capture_output=True, text=True, timeout=5)
                        if result.returncode == 0:
                            return str(ip)
                    except Exception:
                        pass
                    return None
                
                # Limit the number of hosts to scan (prevent overwhelming)
                host_list = list(network.hosts())
                if len(host_list) > 254:
                    self.logger.warning(f"Large network detected ({len(host_list)} hosts). Limiting to first 254 hosts.")
                    host_list = host_list[:254]
                
                with ThreadPoolExecutor(max_workers=50) as executor:
                    futures = [executor.submit(ping_host, ip) for ip in host_list]
                    for future in futures:
                        try:
                            result = future.result(timeout=10)
                            if result:
                                hosts.append(result)
                        except Exception:
                            continue
            else:
                # Single host
                self.logger.info(f"Testing single host: {target}")
                if self._ping_single_host(target):
                    hosts = [target]
                else:
                    self.logger.warning(f"Host {target} appears to be down or not responding to ping")
                    # Still add it to scan in case ping is blocked
                    hosts = [target]
            
        except Exception as e:
            self.logger.error(f"Error in host discovery: {str(e)}")
            # Fallback to single host
            hosts = [target.split('/')[0]]
        
        self.logger.info(f"Discovered {len(hosts)} live hosts")
        return hosts
    
    def _ping_single_host(self, host):
        """Ping a single host"""
        try:
            if platform.system().lower() == 'windows':
                cmd = ['ping', '-n', '1', '-w', '1000', host]
            else:
                cmd = ['ping', '-c', '1', '-W', '1', host]
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=5)
            return result.returncode == 0
        except Exception:
            return False
    
    def _port_scan(self, host):
        """Scan common ports on a host"""
        open_ports = []
        
        def scan_port(port):
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(2)
                result = sock.connect_ex((host, port))
                sock.close()
                if result == 0:
                    return port
            except Exception:
                pass
            return None
        
        try:
            with ThreadPoolExecutor(max_workers=50) as executor:
                futures = [executor.submit(scan_port, port) for port in self.common_ports]
                for future in futures:
                    try:
                        result = future.result(timeout=5)
                        if result:
                            open_ports.append(result)
                    except Exception:
                        continue
        except Exception as e:
            self.logger.error(f"Error during port scanning: {str(e)}")
        
        self.logger.info(f"Found {len(open_ports)} open ports on {host}")
        return sorted(open_ports)
    
    def _enumerate_services(self, host, ports):
        """Enumerate services on open ports"""
        services = {}
        
        for port in ports:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(3)
                sock.connect((host, port))
                
                # Try to grab banner
                banner = ""
                try:
                    if port in [80, 443, 8080]:
                        sock.send(b"HEAD / HTTP/1.0\r\n\r\n")
                    elif port == 21:
                        pass  # FTP sends banner automatically
                    elif port == 22:
                        pass  # SSH sends banner automatically
                    elif port == 25:
                        sock.send(b"EHLO test\r\n")
                    
                    banner = sock.recv(1024).decode('utf-8', errors='ignore')
                except Exception:
                    pass
                
                services[port] = {
                    'service': self._identify_service(port),
                    'banner': banner.strip()[:200]  # Limit banner length
                }
                sock.close()
            except Exception:
                services[port] = {
                    'service': self._identify_service(port),
                    'banner': ''
                }
        
        return services
    
    def _identify_service(self, port):
        """Identify service based on port number"""
        service_map = {
            21: 'FTP', 22: 'SSH', 23: 'Telnet', 25: 'SMTP', 53: 'DNS',
            80: 'HTTP', 110: 'POP3', 135: 'RPC', 139: 'NetBIOS', 143: 'IMAP',
            443: 'HTTPS', 445: 'SMB', 993: 'IMAPS', 995: 'POP3S',
            1723: 'PPTP', 3306: 'MySQL', 3389: 'RDP', 5432: 'PostgreSQL',
            5900: 'VNC', 8080: 'HTTP-Alt'
        }
        return service_map.get(port, 'Unknown')
    
    def _enumerate_smb(self, host):
        """Enumerate SMB shares and information"""
        smb_info = {
            'shares': [],
            'os_info': '',
            'domain_info': ''
        }
        
        try:
            if platform.system().lower() == 'windows':
                # Windows net command
                result = subprocess.run(['net', 'view', f'\\\\{host}'], 
                                      capture_output=True, text=True, timeout=10)
            else:
                # Try smbclient if available
                try:
                    result = subprocess.run(['smbclient', '-L', host, '-N'], 
                                          capture_output=True, text=True, timeout=10)
                except FileNotFoundError:
                    self.logger.warning("smbclient not found. Install with: sudo apt install samba-client")
                    return smb_info
            
            if result.returncode == 0:
                # Parse shares from output
                lines = result.stdout.split('\n')
                for line in lines:
                    if 'Disk' in line or 'Print' in line:
                        parts = line.split()
                        if parts:
                            share_name = parts[0]
                            smb_info['shares'].append(share_name)
        except Exception as e:
            self.logger.debug(f"SMB enumeration failed: {str(e)}")
        
        return smb_info
    
    def _enumerate_ldap(self, host):
        """Enumerate LDAP information"""
        ldap_info = {
            'base_dn': '',
            'naming_contexts': [],
            'domain_info': ''
        }
        
        # Basic LDAP enumeration - placeholder for now
        # In a real implementation, you'd use python-ldap or ldap3
        self.logger.debug(f"LDAP enumeration for {host} - not implemented yet")
        
        return ldap_info
