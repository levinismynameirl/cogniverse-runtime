"""
Demo script for Mini GPT Assistant.
Tests installation and creates sample data.
"""

import os
import sys
import json
from pathlib import Path

def test_imports():
    """Test if all required packages can be imported."""
    print("🧪 Testing package imports...")
    
    packages = [
        ('torch', 'PyTorch'),
        ('transformers', 'Transformers'),
        ('datasets', 'Datasets'),
        ('requests', 'Requests'),
        ('colorama', 'Colorama')
    ]
    
    failed_imports = []
    
    for package, name in packages:
        try:
            __import__(package)
            print(f"  ✅ {name}")
        except ImportError as e:
            print(f"  ❌ {name}: {e}")
            failed_imports.append(package)
    
    if failed_imports:
        print(f"\n❌ Failed to import: {', '.join(failed_imports)}")
        print("Run: pip install -r requirements.txt")
        return False
    
    print("✅ All packages imported successfully!")
    return True

def test_config():
    """Test configuration loading."""
    print("\n🧪 Testing configuration...")
    
    try:
        import config
        print(f"  ✅ Model name: {config.MODEL_NAME}")
        print(f"  ✅ Use GPU: {config.USE_GPU}")
        print(f"  ✅ Allow internet: {config.ALLOW_INTERNET}")
        
        if config.MODEL_NAME == "PLACEHOLDER":
            print("  ⚠️  WARNING: MODEL_NAME is still 'PLACEHOLDER'")
            print("     Please change it in config.py to a real model like 'distilgpt2'")
            return False
        elif config.MODEL_NAME == "distilgpt2":
            print("  ✅ Using recommended default model: distilgpt2")
        
        return True
    except Exception as e:
        print(f"  ❌ Config error: {e}")
        return False

def create_sample_data():
    """Create sample training data."""
    print("\n🧪 Creating sample data...")
    
    try:
        # Create data directory
        data_dir = Path("data")
        data_dir.mkdir(exist_ok=True)
        
        # Create sample dataset
        sample_data = {
            "conversations": [
                {
                    "input": "Hello, how are you?",
                    "output": "Hello! I'm doing well, thank you for asking. How can I help you today?"
                },
                {
                    "input": "What can you do?",
                    "output": "I'm an AI assistant that can help with various tasks like answering questions, having conversations, and providing information."
                },
                {
                    "input": "Tell me about yourself",
                    "output": "I'm a local AI assistant running on your computer. I can chat with you, answer questions, and help with various tasks while keeping your data private."
                },
                {
                    "input": "What model are you using?",
                    "output": "I'm running on the distilgpt2 model by default, which is a lightweight version of GPT-2 that's perfect for local conversations."
                }
            ]
        }
        
        # Save sample data
        with open(data_dir / "sample_conversations.json", "w", encoding="utf-8") as f:
            json.dump(sample_data, f, indent=2, ensure_ascii=False)
        
        print(f"  ✅ Created sample data in {data_dir}/sample_conversations.json")
        return True
        
    except Exception as e:
        print(f"  ❌ Failed to create sample data: {e}")
        return False

def test_model_availability():
    """Test if the configured model is available."""
    print("\n🧪 Testing model availability...")
    
    try:
        import config
        from transformers import AutoTokenizer
        
        print(f"  🔍 Checking model: {config.MODEL_NAME}")
        
        # For distilgpt2, this is very likely to work
        if config.MODEL_NAME == "distilgpt2":
            print("  ✅ distilgpt2 is a standard model and should download automatically")
            print("  ℹ️  Model will be downloaded on first use (requires internet)")
            return True
        
        # Try to load tokenizer for other models (this will download if needed)
        print("  ⏳ Attempting to verify model (this may download files)...")
        tokenizer = AutoTokenizer.from_pretrained(config.MODEL_NAME)
        print(f"  ✅ Model '{config.MODEL_NAME}' is available!")
        
        return True
        
    except Exception as e:
        print(f"  ❌ Model check failed: {e}")
        print(f"  💡 Try using the default model 'distilgpt2'")
        return False

def main():
    """Run all tests."""
    print("🚀 Mini GPT Assistant - Demo & Testing")
    print("=" * 50)
    
    all_passed = True
    
    # Test imports
    if not test_imports():
        all_passed = False
    
    # Test configuration
    if not test_config():
        all_passed = False
    
    # Create sample data
    if not create_sample_data():
        all_passed = False
    
    # Test model (optional, can be slow)
    print(f"\n🤔 Would you like to test model availability? (This may download files)")
    response = input("Test model? (y/N): ").strip().lower()
    if response in ['y', 'yes']:
        if not test_model_availability():
            all_passed = False
    else:
        print("  ⏭️  Skipping model test")
    
    print("\n" + "=" * 50)
    if all_passed:
        print("🎉 All tests passed! You're ready to use the assistant.")
        print("Run: python main.py (or double-click run_assistant.bat)")
        print("")
        print("💡 Default setup uses distilgpt2 model which will auto-download")
    else:
        print("❌ Some tests failed. Please fix the issues above.")
        print("💡 Most common fix: Make sure MODEL_NAME = 'distilgpt2' in config.py")
    
    print("=" * 50)
    input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()