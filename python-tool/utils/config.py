"""
Configuration management for the penetration testing tool
"""

import json
from pathlib import Path

class Config:
    def __init__(self, config_file='config/default.json'):
        self.config_file = Path(config_file)
        self.config = self._load_config()
    
    def _load_config(self):
        """Load configuration from file"""
        if self.config_file.exists():
            with open(self.config_file, 'r') as f:
                return json.load(f)
        else:
            # Return default configuration
            return {
                'scanning': {
                    'timeout': 5,
                    'threads': 50,
                    'common_ports': [21, 22, 23, 25, 53, 80, 110, 135, 139, 143, 443, 445, 993, 995, 1723, 3306, 3389, 5432, 5900, 8080]
                },
                'exploitation': {
                    'enabled': False,
                    'safe_mode': True
                },
                'reporting': {
                    'formats': ['html', 'json', 'markdown'],
                    'include_screenshots': False
                }
            }
    
    def get(self, key, default=None):
        """Get configuration value"""
        keys = key.split('.')
        value = self.config
        
        for k in keys:
            if isinstance(value, dict) and k in value:
                value = value[k]
            else:
                return default
        
        return value
    
    def save(self):
        """Save configuration to file"""
        self.config_file.parent.mkdir(exist_ok=True)
        with open(self.config_file, 'w') as f:
            json.dump(self.config, f, indent=2)
