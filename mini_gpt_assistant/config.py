"""
Cogniverse Runtime Assistant - Configuration
============================================
Simple configuration file for your AI assistant.
Only change settings if you know what you're doing!
"""

# =============================================================================
# MODEL SETTINGS - MAIN CONFIGURATION
# =============================================================================

# Which AI model to use (this is the most important setting!)
MODEL_NAME = "distilgpt2"  # Default: fast, lightweight, good for beginners

# Other good options to try:
# MODEL_NAME = "gpt2"                      # Larger, more capable
# MODEL_NAME = "microsoft/DialoGPT-medium" # Better for conversations
# MODEL_NAME = "facebook/opt-350m"         # Alternative option
# If you have your own model, run setup.bat and place the files in the models/ directory then rename the MODEL_NAME here.
# =============================================================================
# PERFORMANCE SETTINGS
# =============================================================================

# GPU Settings (automatic GPU detection)
USE_GPU = True           # Set to False if you have GPU problems
GPU_MEMORY_LIMIT = None  # None = use all available GPU memory (in GB)

# Response Settings
MAX_RESPONSE_LENGTH = 150    # How long responses can be
RESPONSE_CREATIVITY = 0.3    # 0.1 = boring, 1.0 = very creative
CONVERSATION_MEMORY = 10      # How many exchanges to remember

# =============================================================================
# FEATURES
# =============================================================================

# Internet Search (requires internet connection)
ENABLE_WEB_SEARCH = True  # Set to False to disable internet features

# Logging (saves your conversations)
ENABLE_LOGGING = True     # Set to False to disable conversation logs
LOG_FILE = "logs/assistant.log"

# =============================================================================
# ADVANCED SETTINGS (Don't change unless you know what you're doing!)
# =============================================================================

# Text Generation Parameters
TEMPERATURE = RESPONSE_CREATIVITY  # Don't change this
TOP_P = 0.9
TOP_K = 50
DO_SAMPLE = True
PAD_TOKEN_ID = 50256
REPETITION_PENALTY = 1.1
LENGTH_PENALTY = 1.0

# GPU Technical Settings
GPU_DEVICE = 0 # Which GPU to use (0 = first GPU)

TORCH_DTYPE = "float16"

# Logging Technical Settings
LOG_LEVEL = "INFO"
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"

# Conversation Technical Settings
MAX_LENGTH = MAX_RESPONSE_LENGTH  # Don't change this
MAX_CONVERSATION_HISTORY = CONVERSATION_MEMORY  # Don't change this
CONVERSATION_SEPARATOR = "\n\nHuman: "
ASSISTANT_PREFIX = "\n\nAssistant: "
ALLOW_INTERNET = ENABLE_WEB_SEARCH  # Don't change this

# Web Search Technical Settings
SEARCH_API_URL = "https://api.duckduckgo.com/"
MAX_SEARCH_RESULTS = 3
SEARCH_TIMEOUT = 10

# Training Technical Settings (for advanced users only)
TRAINING_DATA_PATH = "data/training_data.json"
OUTPUT_DIR = "models/fine_tuned"
LEARNING_RATE = 1e-5
NUM_TRAIN_EPOCHS = 1
PER_DEVICE_TRAIN_BATCH_SIZE = 2
SAVE_STEPS = 1000
LOGGING_STEPS = 100
GRADIENT_ACCUMULATION_STEPS = 8
MAX_GRAD_NORM = 1.0
WARMUP_STEPS = 500
WEIGHT_DECAY = 0.01
DATALOADER_NUM_WORKERS = 0
