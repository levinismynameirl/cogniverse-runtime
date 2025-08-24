# Cogniverse Runtime Assistant 🌟

The official runtime environment for the Cogniverse AI marketplace. This lightweight, universal runtime app can run any compatible AI model you download from the upcoming Cogniverse marketplace or compatible models from Hugging Face, Facebook, and OpenAI.

## 🚀 About Cogniverse

**Cogniverse** is a revolutionary AI marketplace where creators can upload, share, and sell their AI models. Users can discover cutting-edge AI models for various tasks and run them locally using this runtime assistant.

### 🎯 Current Features

- **Universal Model Runtime**: Supports most transformer-based models
- **Marketplace Ready**: Designed for seamless integration with Cogniverse marketplace
- **Local Execution**: Run models entirely on your hardware for privacy
- **Easy Model Switching**: Change models with simple configuration edits
- **Conversation History**: Maintains context across sessions
- **Logging**: Full interaction logging for debugging and analysis
- **Windows Optimized**: Built specifically for Windows PowerShell environments
- **GPU Diagnostics**: Built-in tools to check GPU compatibility and performance
- **Installation Testing**: Automated testing to verify setup is working correctly

### 🔮 Coming Soon

- **Official Cogniverse Marketplace**: Browse and download advanced AI models
- **One-Click Model Installation**: Direct marketplace integration
- **Premium Models**: Access to high-performance commercial models
- **Model Ratings & Reviews**: Community-driven model discovery
- **Automatic Updates**: Keep your models up to date

## 📋 System Requirements

- **OS**: Windows 10/11 
- **Python**: 3.11 or higher
- **RAM**: 10GB minimum available (24GB+ recommended for larger models)
- **Storage**: 2-10GB depending on model size
- **GPU**: Optional but recommended - 4GB+ VRAM for GPU acceleration

## 🛠️ Installation

### Simple 3-Step Setup

1. **Download and Extract**:
   - Download the Cogniverse Runtime
   - Extract to your preferred location (e.g., `C:\cogniverse-runtime`)

2. **Run Setup**:
   ```
   Double-click setup.bat
   ```
   This will automatically:
   - Create Python virtual environment
   - Upgrade pip to latest version
   - Install all required dependencies
   - Set up the runtime environment
   - Configure distilgpt2 as the default model

3. **Launch the Assistant**:
   ```
   Double-click run_assistant.bat
   ```

That's it! The runtime comes pre-configured with distilgpt2 and will auto-download the model on first use.

## 🧪 Diagnostic and Testing Tools

### Demo Script (`demo.py`)
Tests your installation and creates sample data:

```bash
python demo.py
```

**What it does:**
- ✅ Tests all package imports (PyTorch, Transformers, etc.)
- ✅ Verifies configuration loading
- ✅ Creates sample training data in `data/` folder
- ✅ Tests model availability and download
- ✅ Provides troubleshooting information

**When to use:**
- After initial setup to verify everything works
- Before starting the assistant for the first time
- When troubleshooting installation issues

### GPU Diagnostic (`check_gpu.py`)
Comprehensive GPU compatibility and performance check:

```bash
python check_gpu.py
```

**What it reports:**
- 🔍 CUDA availability and version
- 🔍 GPU device information and memory
- 🔍 PyTorch GPU support status
- 🔍 Memory allocation testing
- 🔍 NVIDIA driver status via `nvidia-smi`

**Sample output:**
```
🔍 GPU Diagnostic Check
==================================================
PyTorch version: 2.7.1+cu118
CUDA available: True
CUDA version: 11.8
Number of GPUs: 1
GPU 0: NVIDIA GeForce RTX 3080 (10.0GB)
✅ GPU memory allocation test passed
```

**When to use:**
- When experiencing GPU-related errors
- To check if GPU acceleration is properly configured
- Before running large models that require significant VRAM
- When deciding between CPU and GPU modes

### Quick Troubleshooting Workflow

1. **Installation Issues**: Run `python demo.py`
2. **GPU Problems**: Run `python check_gpu.py`  
3. **Model Errors**: Check the error-specific guidance in `run_assistant.bat`
4. **Still Having Issues**: Check `logs/assistant.log` for detailed errors

## 🎯 Using Different Models

### Default Setup (Pre-configured)

The runtime comes **pre-configured** with `distilgpt2`, a lightweight and fast model perfect for beginners:

- **Model**: `distilgpt2` (82M parameters, ~250MB)
- **Auto-download**: Downloads automatically on first use
- **Performance**: Fast responses, low memory usage
- **Perfect for**: First-time users, testing, lightweight conversations

### Easy Model Switching (4 Steps)

Want to use a different model? Here's how:

1. **Choose your model approach**:
   - **Automatic download** (recommended): Use model names like `"gpt2"`
   - **Manual download**: Download files and place in `models/` folder

2. **For automatic download** (easiest):
   - Open `config.py` in Notepad
   - Change `MODEL_NAME = "distilgpt2"` to `MODEL_NAME = "gpt2"`
   - Save and run the assistant

3. **For manual download**:
   - Create a `models` folder in `mini_gpt_assistant` directory
   - Download model files and place them in `models/your_model_name/`
   - Update `config.py`: `MODEL_NAME = "models/your_model_name"`

4. **Run the assistant**:
   ```
   Double-click run_assistant.bat
   ```

### Recommended Models

#### Ready to Use (Auto-download)
```python
# Edit config.py - these will auto-download on first use
MODEL_NAME = "distilgpt2"              # Default - Lightweight, fast (250MB)
MODEL_NAME = "gpt2"                    # Standard GPT-2 (500MB)
MODEL_NAME = "microsoft/DialoGPT-medium"  # Conversation-focused (350MB)
```

#### Popular Model Examples
```python
# Lightweight models (good for limited hardware)
MODEL_NAME = "distilgpt2"              # 82M parameters, ~250MB - DEFAULT
MODEL_NAME = "gpt2"                    # 124M parameters, ~500MB

# Conversation models
MODEL_NAME = "microsoft/DialoGPT-medium"  # 117M parameters, optimized for chat
MODEL_NAME = "microsoft/DialoGPT-large"   # 345M parameters, better responses

# More capable models (require more resources)
MODEL_NAME = "gpt2-medium"             # 345M parameters, ~1.5GB
MODEL_NAME = "facebook/opt-350m"       # Facebook's OPT model
```

### Model Setup Process

**Quick Setup with Bat Files:**

1. **Test your setup** with `python demo.py` (optional)
2. **Check GPU** (optional) with `python check_gpu.py`
3. **Edit config.py** if you want a different model - open with Notepad and change `MODEL_NAME = "distilgpt2"` to your chosen model
4. **Double-click run_assistant.bat** to start

**Example for beginners (already done by default):**
- The runtime is pre-configured with `distilgpt2`
- Just double-click `run_assistant.bat` to start!
- The model will auto-download on first use

## ⚙️ Configuration Options

Edit `config.py` to customize your experience:

```python
# Model Configuration - PRE-CONFIGURED
MODEL_NAME = "distilgpt2"           # Default model (already set!)

# Performance Settings
USE_GPU = True                      # Set to False if no GPU or having issues
MAX_LENGTH = 150                    # Response length
TEMPERATURE = 0.7                   # Creativity (0.1-1.0)

# Features
ALLOW_INTERNET = True               # Enable web search
ENABLE_LOGGING = True               # Log conversations
MAX_CONVERSATION_HISTORY = 5        # Memory depth
```

## 🚀 Quick Start Guide

### First Time Setup

1. **Double-click setup.bat** - This installs everything automatically

2. **Launch the assistant**:
   ```
   Double-click run_assistant.bat
   ```

3. **Start chatting**:
   ```
   🤖 Cogniverse Runtime Assistant
   ============================================
   Model: distilgpt2
   Marketplace: Coming Soon!
   
   You: Hello! What can you do?
   Assistant: Hi! I'm your AI assistant running on the Cogniverse runtime...
   ```

**That's it!** No configuration needed - distilgpt2 is pre-configured and ready to go.

### Available Commands

- `help` - Show available commands
- `status` - Display current model and settings
- `clear` - Clear conversation history
- `history` - Show past conversations
- `quit/exit/bye` - End session

## 🔧 Troubleshooting

### Step-by-Step Troubleshooting

1. **First, run diagnostics**:
   ```bash
   python demo.py        # Tests everything
   python check_gpu.py   # If you have GPU issues
   ```

2. **Check the specific error** in `run_assistant.bat` output

3. **Review detailed logs** in `logs/assistant.log`

### Common Issues and Solutions

#### Model Download Issues
**Problem**: First-time download fails or is slow

**Solutions**:
- Check internet connection
- Wait for download to complete (distilgpt2 is ~250MB)
- Try again - Hugging Face servers can be busy
- Model files are cached in `%USERPROFILE%\.cache\huggingface`

#### Memory/GPU Errors
**Problem**: Not enough VRAM or system RAM

**Solutions**:
- Default distilgpt2 should work on most systems
- Disable GPU: Set `USE_GPU = False` in config.py
- Close other applications
- Run `python check_gpu.py` to diagnose GPU issues

#### Import/Dependency Errors
**Problem**: Missing packages or environment issues

**Solutions**:
- Rerun setup: `setup.bat`
- Reinstall dependencies: `pip install -r requirements.txt`
- Check Python version: `python --version` (needs 3.11+)
- Run `python demo.py` to identify specific missing packages

#### GPU Not Detected
**Problem**: GPU available but not being used

**Solutions**:
- Run `python check_gpu.py` for detailed GPU diagnosis
- Install CUDA-enabled PyTorch: 
  ```bash
  pip uninstall torch torchvision torchaudio
  pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
  ```
- Update NVIDIA drivers
- Set `USE_GPU = False` in config.py to use CPU

## 📂 Project Structure

```
cogniverse-runtime/
├── mini_gpt_assistant/
│   ├── config.py                 # Configuration settings ⚙️
│   ├── main.py                   # Main runtime application
│   ├── demo.py                   # Installation testing script 🧪
│   ├── check_gpu.py              # GPU diagnostic tool 🔍
│   ├── requirements.txt          # Dependencies
│   ├── setup.bat                 # Setup script
│   ├── run_assistant.bat         # Launch script
│   ├── tools/
│   │   ├── __init__.py
│   │   └── websearch.py          # Web search functionality
│   ├── logs/
│   │   └── assistant.log         # Conversation logs
│   ├── data/                     # Training data (created by demo.py)
│   └── models/                   # Local models (create when needed)
└── README.md                     # This file
```

## 🌐 The Cogniverse Ecosystem

### Current Status: Beta Runtime
- ✅ Universal model runtime
- ✅ Hugging Face model support
- ✅ Local execution and privacy
- ✅ Easy configuration and setup
- ✅ Built-in diagnostics and testing
- ✅ GPU acceleration support
- ✅ Pre-configured with distilgpt2

### Coming Soon: Full Marketplace
- 🔄 Official Cogniverse marketplace launch
- 🔄 One-click model downloads
- 🔄 Premium and specialized models
- 🔄 Community ratings and reviews
- 🔄 Automatic model updates
- 🔄 Model performance analytics

### Vision: AI for Everyone
The Cogniverse platform aims to democratize AI by making advanced models accessible to everyone, from hobbyists to enterprises, through an easy-to-use marketplace and runtime environment.

## 🔒 Privacy & Security

- **Local Execution**: All models run on your hardware
- **No Data Transmission**: Conversations stay on your device
- **Optional Internet**: Web search can be disabled
- **Full Logging Control**: Enable/disable conversation logging
- **Open Source Runtime**: Transparent and auditable code

## 🤝 Community & Support

### Getting Help (Follow This Order)
1. **Run diagnostics**: `python demo.py` and `python check_gpu.py`
2. **Check troubleshooting section** above for your specific error
3. **Review logs** in `logs/assistant.log` for detailed error information
4. **Verify requirements**: Python 3.11+, sufficient RAM/storage
5. **Try the default**: Make sure `MODEL_NAME = "distilgpt2"` in config.py

### Contributing
- Report bugs and suggest features
- Share compatible models
- Improve documentation
- Contribute to the runtime codebase

### Preparing for Marketplace Launch
Stay tuned for the official Cogniverse marketplace where you'll be able to:
- Browse thousands of AI models
- Download with one click
- Rate and review models
- Upload your own creations
- Earn from model sales

## 📄 License

This project is provided under an open-source license for the runtime environment. Individual AI models may have their own licensing terms.

---

**Ready to explore the future of AI?** 🚀  
*Your gateway to the Cogniverse ecosystem starts here.*

**Quick Start Checklist:**
- [ ] Run `setup.bat`
- [ ] Run `python demo.py` (optional but recommended)
- [ ] Run `run_assistant.bat` (distilgpt2 is already configured!)
- [ ] Start chatting!

**No configuration needed - distilgpt2 comes pre-configured and ready to use!**
