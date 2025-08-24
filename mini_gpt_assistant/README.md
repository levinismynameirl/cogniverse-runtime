# Mini GPT Assistant

A lightweight, local AI assistant built with Python and Hugging Face Transformers. This assistant runs entirely offline by default and can optionally be configured to use internet search capabilities.

## 🚀 Features

- **Lightweight AI Model**: Uses `distilgpt2` for fast inference on consumer hardware
- **Offline Operation**: Works completely offline by default
- **Conversation History**: Maintains context across conversations
- **Logging**: All interactions are logged to `logs/assistant.log`
- **Optional Web Search**: Can be enabled for internet-based queries
- **Fine-tuning Support**: Train the model on custom datasets
- **Windows PowerShell Ready**: Optimized for Windows environments
- **Colorized Output**: Beautiful console interface with colored text

## 📋 Requirements

- Python 3.11 or higher
- Windows 10/11 (optimized for PowerShell)
- At least 4GB RAM (8GB recommended)
- 2GB free disk space for models

## 🛠️ Installation

### 1. Clone or Download the Project

```powershell
# Navigate to your desired directory
cd C:\
git clone <repository-url> mini_gpt_assistant
# Or download and extract the ZIP file
```

### 2. Set Up Python Virtual Environment

```powershell
# Navigate to the project directory
cd mini_gpt_assistant

# Create virtual environment
python -m venv venv

# Activate virtual environment (PowerShell)
.\venv\Scripts\Activate.ps1

# If you get execution policy error, run:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
(if you still get errors run VSC as administrator)
```

### 3. Install Dependencies

```powershell
# Install all required packages
pip install -r requirements.txt
```

The installation will download the following packages:
- `torch` - PyTorch for deep learning
- `transformers` - Hugging Face transformers library
- `datasets` - For dataset handling
- `requests` - For web search functionality
- `colorama` - For colored console output
- Other supporting libraries

## 🎯 Quick Start

### Basic Usage

```powershell
# Make sure virtual environment is activated
.\venv\Scripts\Activate.ps1

# Run the assistant
python main.py
```

### First Run Experience

When you first run the assistant:
1. It will download the `distilgpt2` model (~250MB)
2. The model will be cached locally for future use
3. You'll see a welcome message with available commands

### Example Conversation

```
🤖 Mini GPT Assistant
============================================
Welcome! I'm your local AI assistant.
Model: distilgpt2
Internet: Disabled
Type 'quit', 'exit', or 'bye' to end the conversation.

You: Hello! What can you help me with?
Assistant: Hello! I'm here to help you with a variety of tasks. I can assist with answering questions, explaining concepts, helping with creative writing, providing information on various topics, and having general conversations. What would you like to know or discuss today?

You: Explain quantum computing in simple terms
Assistant: Quantum computing is like having a super-powered computer that works differently from regular computers. While normal computers use bits that are either 0 or 1, quantum computers use "qubits" that can be 0, 1, or both at the same time. This allows them to solve certain complex problems much faster than traditional computers.
```

## ⚙️ Configuration

### Enabling Internet Search

To enable web search capabilities:

1. Edit `config.py`:
```python
ALLOW_INTERNET = True  # Change from False to True 
# Tip: If you can't find allow internet, press Ctrl+F and you can search there. Must be in the config.py file.
```

2. Restart the assistant:
```powershell
python main.py
```

Now you can ask questions like:
- "Search for latest news about AI"
- "What's the weather today?"
- "Look up information about Python programming"

### Model Configuration

You can switch to a different model by editing `config.py`:

```python
# Options:
MODEL_NAME = "distilgpt2"           # Default, fast and lightweight
MODEL_NAME = "facebook/opt-125m"    # Alternative lightweight model
MODEL_NAME = "gpt2"                 # Larger but more capable
```

### Other Settings

In `config.py` you can also adjust:
- `MAX_LENGTH`: Response length (default: 150)
- `TEMPERATURE`: Response creativity (default: 0.7)
- `MAX_CONVERSATION_HISTORY`: Number of exchanges to remember (default: 10)

## 🎓 Fine-tuning the Model

### Create Sample Training Data

```powershell
# Generate sample training dataset
python train.py --create-sample
```

This creates `data/sample_training_data.json` with example conversations.

### Train on Custom Data

#### Using JSON Format

Create a JSON file with your training data:

```json
[
  {
    "text": "Human: Your question here\nAssistant: The response here"
  },
  {
    "text": "Human: Another question\nAssistant: Another response"
  }
]
```

Then train:

```powershell
python train.py --data your_data.json --epochs 3
```

#### Using Text Format

Create a text file with your content and train:

```powershell
python train.py --data your_text_file.txt --epochs 3
```

#### Training Options

```powershell
# Full training command with options
python train.py --data data/sample_training_data.json ^
                --epochs 5 ^
                --lr 0.00005 ^
                --batch-size 2 ^
                --output models/my_custom_model
```

### Using Your Fine-tuned Model

After training, update `config.py`:

```python
MODEL_NAME = "models/fine_tuned_20240823_143022"  # Use your model path
```

## 📝 Available Commands

While chatting with the assistant, you can use these commands:

- `help` - Show available commands
- `clear` - Clear conversation history
- `history` - Show past conversations
- `status` - Show assistant status and settings
- `quit`, `exit`, `bye` - End the conversation

## 📂 Project Structure

```
mini_gpt_assistant/
├── config.py              # Configuration settings
├── main.py                 # Main assistant application
├── train.py                # Model fine-tuning script
├── requirements.txt        # Python dependencies
├── README.md               # This file
├── tools/
│   ├── __init__.py
│   └── websearch.py        # Web search functionality
├── logs/
│   └── assistant.log       # Conversation logs
├── data/                   # Training data (created when needed)
└── models/                 # Fine-tuned models (created when training)
```

## 🔧 Troubleshooting

### Common Issues

#### PowerShell Execution Policy Error
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

#### Virtual Environment Not Activating
```powershell
# Try this alternative activation method
venv\Scripts\activate.bat
```

#### CUDA/GPU Issues
The assistant is configured to work on CPU by default. If you have a compatible NVIDIA GPU:

1. Install CUDA-enabled PyTorch:
```powershell
pip uninstall torch
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

#### Out of Memory Errors
If you encounter memory issues:

1. Reduce batch size in `config.py`:
```python
PER_DEVICE_TRAIN_BATCH_SIZE = 1  # Reduce from 4 to 1
```

2. Use a smaller model:
```python
MODEL_NAME = "distilgpt2"  # Smallest option
```

#### Model Download Issues
If model download fails:

1. Check your internet connection
2. Try using a different model
3. Clear the Hugging Face cache:
```powershell
rm -r $env:USERPROFILE\.cache\huggingface
```

### Getting Help

1. Check the logs in `logs/assistant.log` for detailed error messages
2. Use the `status` command in the assistant to check configuration
3. Ensure all dependencies are correctly installed with `pip list`

## 🔒 Safety and Privacy

### Data Privacy
- **All conversations are stored locally** in `logs/assistant.log`
- **No data is sent to external servers** when internet is disabled
- **Web search data** (when enabled) goes through DuckDuckGo API

### Safety Considerations
- The AI model may occasionally generate inappropriate content
- Always verify information from the assistant, especially with internet search enabled
- Do not share sensitive personal information in conversations
- Regularly review and clean log files if they contain sensitive data

### Responsible Use
- Use the assistant as a helpful tool, not a replacement for human judgment
- Be aware that AI-generated content may contain biases or inaccuracies
- Follow your organization's AI usage policies if using for work

## 🔄 Updates and Maintenance

### Updating Dependencies
```powershell
# Activate virtual environment
.\venv\Scripts\Activate.ps1

# Update packages
pip install --upgrade -r requirements.txt
```

### Clearing Logs
```powershell
# Clear conversation logs
del logs\assistant.log
```

### Backing Up Custom Models
```powershell
# Backup your fine-tuned models
xcopy models backup_models /E /I
```

## 🤝 Contributing

This is a complete, standalone project. You can:

1. Modify the code to add new features
2. Create custom training datasets
3. Experiment with different models
4. Add new tools and capabilities

## 📄 License

This project is provided as-is for educational and personal use. Please respect the licenses of the underlying libraries (PyTorch, Transformers, etc.).

## 🙋‍♀️ Support

If you encounter issues:

1. Check this README for troubleshooting steps
2. Review the configuration in `config.py`
3. Check the logs in `logs/assistant.log`
4. Ensure your Python version is 3.11 or higher

---

**Happy chatting with your local AI assistant!** 🤖✨
