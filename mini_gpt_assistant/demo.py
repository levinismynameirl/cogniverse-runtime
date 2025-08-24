"""
Demo script to test the Mini GPT Assistant installation and create sample data.
Run this script to verify everything is working correctly.
"""

import sys
import os
import json
from pathlib import Path

# Add the current directory to the Python path
sys.path.insert(0, str(Path(__file__).parent))

def test_imports():
    """Test that all required packages can be imported."""
    print("🧪 Testing package imports...")
    
    try:
        import torch
        print(f"✅ PyTorch {torch.__version__}")
        
        import transformers
        print(f"✅ Transformers {transformers.__version__}")
        
        import datasets
        print(f"✅ Datasets {datasets.__version__}")
        
        import requests
        print(f"✅ Requests {requests.__version__}")
        
        import colorama
        print(f"✅ Colorama {colorama.__version__}")
        
        import numpy
        print(f"✅ NumPy {numpy.__version__}")
        
        print("\n🎉 All packages imported successfully!")
        return True
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False

def create_sample_data():
    """Create sample training data for demonstration."""
    print("\n📝 Creating sample training data...")
    
    # Create data directory
    data_dir = Path("data")
    data_dir.mkdir(exist_ok=True)
    
    # Sample conversation data
    sample_conversations = [
        {
            "text": "Human: What is artificial intelligence?\nAssistant: Artificial intelligence (AI) is a branch of computer science that aims to create machines capable of intelligent behavior. It involves developing algorithms and systems that can perform tasks typically requiring human intelligence, such as learning, reasoning, problem-solving, and understanding language."
        },
        {
            "text": "Human: How do neural networks work?\nAssistant: Neural networks are computing systems inspired by biological neural networks. They consist of interconnected nodes (neurons) organized in layers. Each connection has a weight that adjusts as learning proceeds. The network processes information by passing it through these weighted connections, allowing it to recognize patterns and make predictions."
        },
        {
            "text": "Human: What is machine learning?\nAssistant: Machine learning is a subset of artificial intelligence that enables computers to learn and improve from experience without being explicitly programmed. It uses algorithms to analyze data, identify patterns, and make decisions or predictions based on that analysis."
        },
        {
            "text": "Human: Explain deep learning.\nAssistant: Deep learning is a subset of machine learning that uses neural networks with multiple layers (hence 'deep') to model and understand complex patterns in data. These deep neural networks can automatically learn hierarchical representations of data, making them particularly effective for tasks like image recognition, natural language processing, and speech recognition."
        },
        {
            "text": "Human: What are the applications of AI?\nAssistant: AI has numerous applications across various fields including healthcare (medical diagnosis, drug discovery), transportation (autonomous vehicles), finance (fraud detection, algorithmic trading), entertainment (recommendation systems, game AI), customer service (chatbots), and many others. It's increasingly being integrated into everyday technologies to make them smarter and more efficient."
        },
        {
            "text": "Human: How can I get started with Python programming?\nAssistant: To get started with Python programming: 1) Install Python from python.org, 2) Choose a code editor like VS Code or PyCharm, 3) Learn basic syntax and concepts through online tutorials, 4) Practice with small projects, 5) Join Python communities for support. Start with simple programs and gradually work on more complex projects as you build confidence."
        },
        {
            "text": "Human: What's the difference between lists and tuples in Python?\nAssistant: The main differences between lists and tuples in Python are: 1) Mutability - lists are mutable (can be changed) while tuples are immutable (cannot be changed after creation), 2) Syntax - lists use square brackets [] while tuples use parentheses (), 3) Performance - tuples are generally faster for access operations, 4) Use cases - use lists when you need to modify data, use tuples for fixed data like coordinates or database records."
        }
    ]
    
    # Save to JSON file
    json_file = data_dir / "sample_training_data.json"
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(sample_conversations, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Sample training data created: {json_file}")
    
    # Create a simple text file as well
    text_file = data_dir / "sample_text_data.txt"
    with open(text_file, 'w', encoding='utf-8') as f:
        f.write("""The future of artificial intelligence is bright and full of possibilities.
AI technologies are rapidly advancing, making our daily lives more convenient and efficient.
From smart home devices to autonomous vehicles, AI is transforming how we interact with technology.

Machine learning algorithms continue to improve, enabling computers to learn from data without explicit programming.
Deep learning, a subset of machine learning, uses neural networks to solve complex problems.
Natural language processing allows computers to understand and generate human language.

As AI becomes more prevalent, it's important to consider ethical implications and ensure responsible development.
The goal is to create AI systems that benefit humanity while minimizing potential risks.
Education and awareness about AI will be crucial for society to adapt to these technological changes.""")
    
    print(f"✅ Sample text data created: {text_file}")
    return True

def check_model_availability():
    """Check if the default model can be loaded."""
    print("\n🤖 Testing model availability...")
    
    try:
        from transformers import AutoTokenizer
        
        # Test loading the tokenizer (this will download the model if needed)
        model_name = "distilgpt2"
        print(f"Testing model: {model_name}")
        
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        print(f"✅ Model {model_name} is available and ready to use!")
        
        return True
        
    except Exception as e:
        print(f"❌ Model loading error: {e}")
        print("This might happen on first run - the model will be downloaded when you start the assistant.")
        return False

def test_config():
    """Test configuration loading."""
    print("\n⚙️ Testing configuration...")
    
    try:
        import config
        print(f"✅ Model configured: {config.MODEL_NAME}")
        print(f"✅ Internet access: {'Enabled' if config.ALLOW_INTERNET else 'Disabled'}")
        print(f"✅ Max length: {config.MAX_LENGTH}")
        print(f"✅ Log file: {config.LOG_FILE}")
        return True
        
    except Exception as e:
        print(f"❌ Configuration error: {e}")
        return False

def main():
    """Run all tests."""
    print("🚀 Mini GPT Assistant - Installation Test\n")
    print("=" * 50)
    
    all_passed = True
    
    # Test imports
    all_passed &= test_imports()
    
    # Test configuration
    all_passed &= test_config()
    
    # Create sample data
    all_passed &= create_sample_data()
    
    # Test model availability (optional)
    check_model_availability()
    
    print("\n" + "=" * 50)
    
    if all_passed:
        print("🎉 Installation test completed successfully!")
        print("\nNext steps:")
        print("1. Run the assistant: python main.py")
        print("2. Try fine-tuning: python train.py --create-sample")
        print("3. Read the README.md for detailed instructions")
    else:
        print("❌ Some tests failed. Please check the error messages above.")
        print("Make sure all dependencies are installed correctly.")
    
    print("\n💡 Tip: The first run will download the AI model (~250MB)")
    print("   This is normal and only happens once.")

if __name__ == "__main__":
    main()
