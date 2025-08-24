<!-- Use this file to provide workspace-specific custom instructions to Copilot. For more details, visit https://code.visualstudio.com/docs/copilot/copilot-customization#_use-a-githubcopilotinstructionsmd-file -->

# Mini GPT Assistant - Copilot Instructions

This is a Python-based AI assistant project using Hugging Face Transformers. When working with this codebase:

## Project Context
- This is a local AI assistant that runs offline by default
- Uses lightweight models like `distilgpt2` for consumer hardware
- Supports optional internet search capabilities
- Includes fine-tuning functionality for custom datasets
- Optimized for Windows PowerShell environments

## Code Style Guidelines
- Follow PEP 8 Python style guidelines
- Use type hints for function parameters and return values
- Include comprehensive docstrings for all classes and functions
- Handle exceptions gracefully with proper logging
- Use f-strings for string formatting

## Key Dependencies
- `torch` and `transformers` for AI model functionality
- `datasets` for data handling
- `requests` for web search features
- `colorama` for console output formatting

## Architecture Notes
- `main.py` contains the main conversation loop and assistant logic
- `config.py` centralizes all configuration settings
- `train.py` handles model fine-tuning operations
- `tools/websearch.py` provides optional internet search functionality
- All user interactions are logged to `logs/assistant.log`

## When Making Changes
- Ensure backward compatibility with existing configuration
- Test both online and offline modes when modifying web search features
- Validate that model loading works on both CPU and GPU configurations
- Update the README.md if adding new features or changing setup procedures
