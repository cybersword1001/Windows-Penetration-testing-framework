#!/usr/bin/env python3
"""
Test script to verify the Windows Penetration Testing Tool installation
"""

import sys
import os
import subprocess
import importlib

def test_python_version():
    """Test Python version"""
    print("🐍 Testing Python version...")
    if sys.version_info >= (3, 7):
        print(f"✅ Python {sys.version.split()[0]} - OK")
        return True
    else:
        print(f"❌ Python {sys.version.split()[0]} - Need 3.7+")
        return False

def test_system_tools():
    """Test system tools"""
    print("\n🔧 Testing system tools...")
    tools = {
        'ping': 'Host discovery',
        'nmap': 'Advanced scanning (optional)'
    }
    
    results = {}
    for tool, description in tools.items():
        try:
            result = subprocess.run([tool, '--version'], 
                                  capture_output=True, timeout=5)
            if result.returncode == 0:
                print(f"✅ {tool} - {description}")
                results[tool] = True
            else:
                print(f"❌ {tool} - {description}")
                results[tool] = False
        except (subprocess.TimeoutExpired, FileNotFoundError):
            print(f"❌ {tool} - {description} (not found)")
            results[tool] = False
    
    return results

def test_python_modules():
    """Test Python modules"""
    print("\n📦 Testing Python modules...")
    
    required_modules = [
        'socket', 'threading', 'subprocess', 'json', 'pathlib',
        'concurrent.futures', 'ipaddress', 'platform'
    ]
    
    optional_modules = [
        'requests', 'nmap'
    ]
    
    all_good = True
    
    print("Required modules:")
    for module in required_modules:
        try:
            importlib.import_module(module)
            print(f"✅ {module}")
        except ImportError:
            print(f"❌ {module}")
            all_good = False
    
    print("\nOptional modules:")
    for module in optional_modules:
        try:
            importlib.import_module(module)
            print(f"✅ {module}")
        except ImportError:
            print(f"⚠️  {module} (optional)")
    
    return all_good

def test_file_structure():
    """Test file structure"""
    print("\n📁 Testing file structure...")
    
    required_files = [
        'main.py',
        'modules/scanner.py',
        'modules/vulnerability_detector.py',
        'modules/exploiter.py',
        'modules/post_exploit.py',
        'modules/reporter.py',
        'utils/logger.py',
        'utils/config.py'
    ]
    
    all_good = True
    for file_path in required_files:
        if os.path.exists(file_path):
            print(f"✅ {file_path}")
        else:
            print(f"❌ {file_path}")
            all_good = False
    
    return all_good

def test_basic_functionality():
    """Test basic functionality"""
    print("\n🧪 Testing basic functionality...")
    
    try:
        # Test help command
        result = subprocess.run([sys.executable, 'main.py', '--help'], 
                              capture_output=True, text=True, timeout=10)
        if result.returncode == 0:
            print("✅ Help command works")
            return True
        else:
            print("❌ Help command failed")
            print(f"Error: {result.stderr}")
            return False
    except Exception as e:
        print(f"❌ Basic functionality test failed: {str(e)}")
        return False

def main():
    """Main test function"""
    print("🔍 Windows Penetration Testing Tool - Installation Test")
    print("=" * 60)
    
    tests = [
        ("Python Version", test_python_version),
        ("System Tools", test_system_tools),
        ("Python Modules", test_python_modules),
        ("File Structure", test_file_structure),
        ("Basic Functionality", test_basic_functionality)
    ]
    
    results = {}
    for test_name, test_func in tests:
        try:
            results[test_name] = test_func()
        except Exception as e:
            print(f"❌ {test_name} test failed with error: {str(e)}")
            results[test_name] = False
    
    print("\n" + "=" * 60)
    print("📊 Test Results Summary:")
    
    all_passed = True
    for test_name, passed in results.items():
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"{status} {test_name}")
        if not passed:
            all_passed = False
    
    print("\n" + "=" * 60)
    if all_passed:
        print("🎉 All tests passed! The tool should work correctly.")
        print("\n💡 Try running: python3 main.py -t 127.0.0.1 --scan-only -v")
    else:
        print("⚠️  Some tests failed. Please fix the issues above.")
        print("\n🔧 Common fixes:")
        print("   - Install missing tools: sudo apt install nmap samba-client")
        print("   - Install Python modules: pip3 install -r requirements.txt")
        print("   - Check file permissions: chmod +x main.py")

if __name__ == "__main__":
    main()
