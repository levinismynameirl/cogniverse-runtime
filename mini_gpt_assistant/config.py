"""
Configuration settings for the Mini GPT Assistant.
"""

# Model Configuration - UPGRADED TO LARGER MODEL
MODEL_NAME = "PLACEHOLDER"  # Much better for conversations
# Alternative options:
# MODEL_NAME = "facebook/opt-350m"        # Good general model
# MODEL_NAME = "gpt2-medium"              # Larger GPT-2 variant
# MODEL_NAME = "microsoft/DialoGPT-large" # Even better but needs more VRAM

# Generation Parameters - IMPROVED FOR BETTER RESPONSES
MAX_LENGTH = 150
TEMPERATURE = 0.7  # Less random for more coherent responses
TOP_P = 0.9
TOP_K = 50  # Add top-k sampling
DO_SAMPLE = True
PAD_TOKEN_ID = 50256
REPETITION_PENALTY = 1.1  # Prevent repetition
LENGTH_PENALTY = 1.0

# GPU Configuration
USE_GPU = True
GPU_DEVICE = 0
TORCH_DTYPE = "float16"

# Internet Features - FIXED
ALLOW_INTERNET = True

# Logging Configuration
LOG_LEVEL = "INFO"
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
LOG_FILE = "logs/assistant.log"

# Conversation Settings
MAX_CONVERSATION_HISTORY = 5  # Reduced to prevent context pollution
CONVERSATION_SEPARATOR = "\n\nHuman: "
ASSISTANT_PREFIX = "\n\nAssistant: "

# Web Search Configuration - FIXED
SEARCH_API_URL = "https://api.duckduckgo.com/"
MAX_SEARCH_RESULTS = 3
SEARCH_TIMEOUT = 10

# Training Configuration - IMPROVED
TRAINING_DATA_PATH = "data/massive_web_dataset.json"
OUTPUT_DIR = "models/fine_tuned"
LEARNING_RATE = 1e-5  # Much lower for large models
NUM_TRAIN_EPOCHS = 1  # Fewer epochs for large datasets
PER_DEVICE_TRAIN_BATCH_SIZE = 2  # Smaller for larger models
SAVE_STEPS = 1000
LOGGING_STEPS = 100
GRADIENT_ACCUMULATION_STEPS = 8  # Larger effective batch size
MAX_GRAD_NORM = 1.0
WARMUP_STEPS = 500
WEIGHT_DECAY = 0.01
DATALOADER_NUM_WORKERS = 0
