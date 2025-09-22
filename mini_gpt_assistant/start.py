"""
Old start script for Mini GPT Assistant. Run run_assitant.bat instead.
This script requires manual activation of the virtual environment.
"""

import os
import sys
import subprocess
from pathlib import Path

def check_python_version():
    """Check if Python version is compatible."""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 11):
        print(f"❌ Python {version.major}.{version.minor} is not supported.")
        print("Please install Python 3.11 or higher.")
        return False
    print(f"✅ Python {version.major}.{version.minor}.{version.micro}")
    return True

def check_virtual_environment():
    """Check if virtual environment exists and activate it."""
    venv_path = Path("venv")
    
    if not venv_path.exists():
        print("❌ Virtual environment not found.")
        print("Please run setup.bat first or create the environment manually:")
        print("  python -m venv venv")
        return False
    
    # Check if we're already in a virtual environment
    if hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
        print("✅ Virtual environment already active")
        return True
    
    print("ℹ️  Virtual environment found but not active.")
    print("Please activate it first:")
    print("  venv\\Scripts\\activate.bat")
    return False

def check_dependencies():
    """Check if required packages are installed."""
    required_packages = [
        'torch', 'transformers', 'datasets', 'requests', 'colorama'
    ]
    
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package)
        except ImportError:
            missing_packages.append(package)
    
    if missing_packages:
        print(f"❌ Missing packages: {', '.join(missing_packages)}")
        print("Please install dependencies:")
        print("  pip install -r requirements.txt")
        return False
    
    print("✅ All dependencies are installed")
    return True

def main():
    """Main startup function."""
    print("🚀 Mini GPT Assistant - Quick Start")
    print("=" * 40)
    
    # Check Python version
    if not check_python_version():
        input("Press Enter to exit...")
        return
    
    # Check virtual environment
    if not check_virtual_environment():
        input("Press Enter to exit...")
        return
    
    # Check dependencies
    if not check_dependencies():
        input("Press Enter to exit...")
        return
    
    print("\n🎉 All checks passed! Starting the assistant...")
    print("=" * 40)
    
    # Import and run the main assistant
    try:
        from main import main as run_assistant
        run_assistant()
    except KeyboardInterrupt:
        print("\n👋 Goodbye!")
    except ImportError as e:
        print(f"❌ Failed to import assistant: {e}")
        print("Make sure all files are in the correct location.")
        input("Press Enter to exit...")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        print("Check the logs/assistant.log file for more details.")
        input("Press Enter to exit...")

if __name__ == "__main__":
    main()
