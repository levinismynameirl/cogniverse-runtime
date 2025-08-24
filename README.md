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

### 🔮 Coming Soon

- **Official Cogniverse Marketplace**: Browse and download advanced AI models
- **One-Click Model Installation**: Direct marketplace integration
- **Premium Models**: Access to high-performance commercial models
- **Model Ratings & Reviews**: Community-driven model discovery
- **Automatic Updates**: Keep your models up to date

## 📋 System Requirements

- **OS**: Windows 10/11 
- **Python**: 3.11 or higher
- **RAM**: 10GB minimum availbale (24GB+ recommended for larger models)
- **Storage**: 2-10GB depending on model size
- **GPU**: Depends on AI model but most require at least 4gb of VRAM

## 🛠️ Installation

### Simple 3-Step Setup

1. **Download and Extract**:
   - Download the latest Cogniverse runtime release.
   - Extract to your preferred location (e.g., `C:\cogniverse-runtime`)

2. **Run Setup**:
   ```
   Double-click setup.bat
   ```
   This will automatically:
   - Create Python virtual environment
   - Install all required dependencies
   - Set up the runtime environment

3. **Launch the Assistant**:
   ```
   Double-click run_assistant.bat
   ```

That's it! The runtime will download a default model on first launch.

## 🎯 Using Different Models

### Easy Model Setup (3 Steps)

1. **Create a models folder**:
   - Go to the `mini_gpt_assistant` folder
   - Create a new folder called `models` (case sensitive)

2. **Download and place your model**:
   - Download from Hugging Face, OpenAI, Facebook, etc.
   - Put the model files in the `models` folder you just created

3. **Update the config (REQUIRED)**:
   - Double-click `config.py` to open it in Notepad
   - Find the line `MODEL_NAME = "PLACEHOLDER"`
   - Change "PLACEHOLDER" to your exact model name (case sensitive)
   - Save and close

   **Example**: Change `MODEL_NAME = "PLACEHOLDER"` to `MODEL_NAME = "distilgpt2"`

4. **Run the assistant**:
   ```
   Double-click run_assistant.bat
   ```

### Popular Model Examples

#### Hugging Face Models
```python
# Edit config.py
MODEL_NAME = "distilgpt2"              # Lightweight, fast
MODEL_NAME = "gpt2"                    # Standard GPT-2
MODEL_NAME = "microsoft/DialoGPT-medium"  # Conversation-focused
MODEL_NAME = "facebook/opt-125m"       # Facebook's OPT model
```

#### Local Models (Downloaded from Future Marketplace)
```python
# Place model files in models/ folder and reference them:
MODEL_NAME = "models/cogniverse-advanced-chat-v1"
MODEL_NAME = "models/specialized-coding-assistant"
```

### Model Setup Process

**Quick Setup with Bat Files:**

1. **Download a Model** from Hugging Face or other sources
2. **Create models folder** in `mini_gpt_assistant` directory (if it doesn't exist)
3. **Place model files** in the models folder
4. **Edit config.py** - open with Notepad and change `MODEL_NAME` to your model
5. **Double-click run_assistant.bat** to start

**Example:**
- Download `gpt2` model files
- Create `models` folder 
- Put files in `models/gpt2/`
- Change config.py: `MODEL_NAME = "models/gpt2"`
- Double-click `run_assistant.bat`

## ⚙️ Configuration Options

Edit `config.py` to customize your experience:

```python
# Model Configuration
MODEL_NAME = "distilgpt2"           # Your chosen model
USE_GPU = False                     # Set to True for GPU acceleration

# Conversation Settings
MAX_LENGTH = 150                    # Response length
TEMPERATURE = 0.7                   # Creativity (0.1-1.0)
MAX_CONVERSATION_HISTORY = 10       # Memory depth

# Features
ALLOW_INTERNET = False              # Enable web search
ENABLE_LOGGING = True               # Log conversations
```

## 🚀 Quick Start Guide

### First Time Setup

1. **Double-click setup.bat** - This installs everything automatically

2. **IMPORTANT: Configure your model**:
   - Open `config.py` in Notepad
   - Change `MODEL_NAME = "PLACEHOLDER"` to `MODEL_NAME = "distilgpt2"` 
   - Save the file

3. **Double-click run_assistant.bat** - This launches the assistant

4. **Start chatting**:
   ```
   🤖 Cogniverse Runtime Assistant
   ============================================
   Model: distilgpt2
   Marketplace: Coming Soon!
   
   You: Hello! What can you do?
   Assistant: Hi! I'm your AI assistant running on the Cogniverse runtime...
   ```

**That's it!** No PowerShell commands needed - just double-click the bat files.

### Available Commands

- `help` - Show available commands
- `status` - Display current model and settings
- `clear` - Clear conversation history
- `history` - Show past conversations
- `quit/exit/bye` - End session

## 🔧 Troubleshooting

### No Model Detected Error

If you see "ERROR: No model configured!" or something similar, follow these simple steps:

1. **Create models folder**:
   - Go to `mini_gpt_assistant` folder
   - Create a new folder called `models`

2. **Download a model** from Hugging Face:
   - Recommended: `distilgpt2` (lightweight)
   - Alternative: `gpt2` (more capable)  
   - Conversational: `microsoft/DialoGPT-medium`

3. **Update config.py**:
   - Double-click `config.py` to open in Notepad
   - Change: `MODEL_NAME = "PLACEHOLDER"`
   - To: `MODEL_NAME = "distilgpt2"` (or your chosen model)
   - Save the file

4. **Restart the assistant**:
   - Double-click `run_assistant.bat`

### Common Issues

#### Memory Errors
- Use smaller models like `distilgpt2`
- Set `USE_GPU = False` in config.py
- Close other applications to free RAM

#### Download Failures
- Check internet connection
- Try a different model
- Clear cache: `rm -r $env:USERPROFILE\.cache\huggingface`

#### Permission Errors
- Run PowerShell as Administrator
- Set execution policy: `Set-ExecutionPolicy RemoteSigned`

## 📂 Project Structure

```
cogniverse-runtime/
├── mini_gpt_assistant/
│   ├── config.py                 # Configuration settings
│   ├── main.py                   # Main runtime application
│   ├── requirements.txt          # Dependencies
│   ├── setup.bat                 # Setup script
│   ├── run_assistant.bat         # Launch script
│   ├── tools/
│   │   ├── __init__.py
│   │   └── websearch.py          # Web search functionality
│   ├── logs/
│   │   └── assistant.log         # Conversation logs
│   └── models/                   # Local models (create when needed)
└── README.md                     # This file
```

## 🌐 The Cogniverse Ecosystem

### Current Status: Beta Runtime
- ✅ Universal model runtime
- ✅ Hugging Face model support
- ✅ Local execution and privacy
- ✅ Easy configuration and setup

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

### Getting Help
1. Check the troubleshooting section above
2. Review logs in `logs/assistant.log`
3. Ensure your Python version is 3.11+
4. Verify model configuration in `config.py`

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
