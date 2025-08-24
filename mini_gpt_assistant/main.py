"""
Mini GPT Assistant - A lightweight local AI assistant.

This script provides a command-line interface for chatting with a local AI model.
It supports conversation history, logging, and optional internet search capabilities.
"""

import os
import sys
import logging
from datetime import datetime
from typing import List, Dict, Optional
import json

import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
import colorama
from colorama import Fore, Back, Style

import config
from tools.websearch import WebSearchTool


class MiniGPTAssistant:
    """Main assistant class that handles conversation and model interactions."""
    
    def __init__(self):
        """Initialize the assistant with model and configuration."""
        self.setup_logging()
        self.setup_colorama()
        self.conversation_history: List[Dict[str, str]] = []
        
        # Initialize web search tool if internet is enabled
        self.web_search = None
        if config.ALLOW_INTERNET:
            try:
                self.web_search = WebSearchTool()
                self.logger.info("Web search tool initialized")
            except Exception as e:
                self.logger.warning(f"Failed to initialize web search: {e}")
        
        # Load model and tokenizer
        self.load_model()
        
    def setup_logging(self):
        """Configure logging to file and console."""
        os.makedirs(os.path.dirname(config.LOG_FILE), exist_ok=True)
        
        # Create logger
        self.logger = logging.getLogger('MiniGPTAssistant')
        self.logger.setLevel(getattr(logging, config.LOG_LEVEL))
        
        # Create file handler
        file_handler = logging.FileHandler(config.LOG_FILE, encoding='utf-8')
        file_handler.setLevel(logging.INFO)
        
        # Create formatter
        formatter = logging.Formatter(config.LOG_FORMAT)
        file_handler.setFormatter(formatter)
        
        # Add handler to logger
        if not self.logger.handlers:
            self.logger.addHandler(file_handler)
    
    def setup_colorama(self):
        """Initialize colorama for colored console output."""
        colorama.init(autoreset=True)
    
    def load_model(self):
        """Load the AI model and tokenizer."""
        try:
            self.logger.info(f"Loading model: {config.MODEL_NAME}")
            print(f"{Fore.YELLOW}Loading AI model... This may take a moment.{Style.RESET_ALL}")
            
            # Determine device and dtype
            if config.USE_GPU and torch.cuda.is_available():
                device = f"cuda:{config.GPU_DEVICE}"
                torch_dtype = torch.float16 if config.TORCH_DTYPE == "float16" else torch.float32
                device_map = {"": config.GPU_DEVICE}
                print(f"{Fore.GREEN}GPU detected! Using device: {device}{Style.RESET_ALL}")
                self.logger.info(f"Using GPU device: {device}")
            else:
                device = "cpu"
                torch_dtype = torch.float32  # Always use float32 for CPU
                device_map = None
                if config.USE_GPU:
                    print(f"{Fore.YELLOW}GPU requested but not available, falling back to CPU{Style.RESET_ALL}")
                    self.logger.warning("GPU requested but not available, using CPU")
                else:
                    print(f"{Fore.BLUE}Using CPU as configured{Style.RESET_ALL}")
                    self.logger.info("Using CPU as configured")
            
            # Load tokenizer
            self.tokenizer = AutoTokenizer.from_pretrained(config.MODEL_NAME)
            
            # Set pad token if not exists
            if self.tokenizer.pad_token is None:
                self.tokenizer.pad_token = self.tokenizer.eos_token
            
            # Load model with optimized settings for GPU
            self.model = AutoModelForCausalLM.from_pretrained(
                config.MODEL_NAME,
                torch_dtype=torch_dtype,
                device_map=device_map,
                low_cpu_mem_usage=True,  # Optimize memory usage
                trust_remote_code=True   # For some models
            )
            
            # Move model to device if not using device_map
            if device_map is None:
                self.model = self.model.to(device)
            
            # Create text generation pipeline
            self.generator = pipeline(
                "text-generation",
                model=self.model,
                tokenizer=self.tokenizer,
                torch_dtype=torch_dtype,
                device=device if device_map is None else None,
                device_map=device_map
            )
            
            # Display GPU memory info if using CUDA
            if torch.cuda.is_available() and device.startswith('cuda'):
                gpu_memory = torch.cuda.get_device_properties(config.GPU_DEVICE).total_memory / 1024**3
                gpu_memory_used = torch.cuda.memory_allocated(config.GPU_DEVICE) / 1024**3
                print(f"{Fore.GREEN}GPU Memory: {gpu_memory_used:.1f}GB / {gpu_memory:.1f}GB{Style.RESET_ALL}")
                self.logger.info(f"GPU memory usage: {gpu_memory_used:.1f}GB / {gpu_memory:.1f}GB")
            
            device_name = "GPU" if device.startswith('cuda') else "CPU"
            print(f"{Fore.GREEN}Model loaded successfully on {device_name}!{Style.RESET_ALL}")
            self.logger.info(f"Model loaded successfully on {device_name}")
            
        except Exception as e:
            error_msg = f"Failed to load model: {e}"
            self.logger.error(error_msg)
            print(f"{Fore.RED}Error: {error_msg}{Style.RESET_ALL}")
            sys.exit(1)
    
    def generate_response(self, user_input: str) -> str:
        """Generate a response to user input."""
        try:
            # Build conversation context with better formatting
            context = self.build_context(user_input)
            
            # Check if user is asking for web search
            if config.ALLOW_INTERNET and self.web_search and self.should_search_web(user_input):
                search_results = self.web_search.search(user_input)
                if search_results:
                    context += f"\n\nWeb search results: {search_results}"
            
            # Generate response with better parameters
            response = self.generator(
                context,
                max_new_tokens=config.MAX_LENGTH,
                temperature=config.TEMPERATURE,
                top_p=config.TOP_P,
                do_sample=config.DO_SAMPLE,
                pad_token_id=self.tokenizer.eos_token_id,
                eos_token_id=self.tokenizer.eos_token_id,
                num_return_sequences=1,
                repetition_penalty=1.1,
                length_penalty=1.0
            )
            
            # Extract the generated text
            generated_text = response[0]['generated_text']
            
            # Remove the input context to get only the new response
            response_text = generated_text[len(context):].strip()
            
            # Clean up the response
            response_text = self.clean_response(response_text)
            
            return response_text
            
        except Exception as e:
            error_msg = f"Error generating response: {e}"
            self.logger.error(error_msg)
            return f"I apologize, but I encountered an error while generating a response: {e}"
    
    def build_context(self, user_input: str) -> str:
        """Build conversation context from history."""
        context_parts = []
        
        # Add a system prompt to guide the assistant's behavior
        context_parts.append("You are a helpful AI assistant. Please provide clear, concise, and helpful responses to the user's questions.")
        context_parts.append("")  # Empty line for separation
        
        # Add recent conversation history (limit to avoid repetition)
        recent_history = self.conversation_history[-3:]  # Only last 3 exchanges
        for exchange in recent_history:
            context_parts.append(f"Human: {exchange['user']}")
            context_parts.append(f"Assistant: {exchange['assistant']}")
        
        # Add current user input
        context_parts.append(f"Human: {user_input}")
        context_parts.append("Assistant:")
        
        return "\n".join(context_parts)
    
    def clean_response(self, response: str) -> str:
        """Clean up the generated response."""
        if not response:
            return "I'm not sure how to respond to that."
        
        # Remove any remaining conversation markers
        response = response.replace("Human:", "").replace("Assistant:", "")
        
        # Split by common delimiters and take the first coherent part
        for delimiter in ['\n\nHuman:', '\nHuman:', '\n\nAssistant:', '\nAssistant:']:
            if delimiter in response:
                response = response.split(delimiter)[0]
                break
        
        # Clean up line by line
        lines = response.split('\n')
        cleaned_lines = []
        
        for line in lines:
            line = line.strip()
            if line and not line.startswith(('Human:', 'Assistant:', 'You:', 'User:')):
                # Skip repetitive academic titles or weird patterns
                if not any(pattern in line.lower() for pattern in ['professor:', 'dr. dr.', 'university of california' * 3]):
                    cleaned_lines.append(line)
                    
        # Join lines and clean up
        result = ' '.join(cleaned_lines).strip()
        
        # Remove excessive repetition
        words = result.split()
        if len(words) > 10:
            # Check for word repetition and truncate if found
            for i in range(len(words) - 5):
                if words[i:i+3] == words[i+3:i+6]:  # Found 3-word repetition
                    result = ' '.join(words[:i+3])
                    break
        
        # Limit response length
        if len(result) > 300:
            # Find the last complete sentence within limit
            sentences = result[:300].split('.')
            if len(sentences) > 1:
                result = '.'.join(sentences[:-1]) + '.'
            else:
                result = result[:300] + "..."
        
        # Final cleanup
        result = result.strip()
        if not result or len(result) < 3:
            return "Hello! How can I help you today?"
        
        return result
    
    def should_search_web(self, user_input: str) -> bool:
        """Determine if the user input warrants a web search."""
        search_indicators = [
            "search", "look up", "find", "what's", "news", "current", 
            "recent", "today", "latest", "weather", "stock", "price"
        ]
        return any(indicator in user_input.lower() for indicator in search_indicators)
    
    def add_to_history(self, user_input: str, assistant_response: str):
        """Add exchange to conversation history."""
        self.conversation_history.append({
            'user': user_input,
            'assistant': assistant_response,
            'timestamp': datetime.now().isoformat()
        })
        
        # Log the conversation
        self.logger.info(f"User: {user_input}")
        self.logger.info(f"Assistant: {assistant_response}")
    
    def display_welcome(self):
        """Display welcome message."""
        print(f"{Fore.CYAN}{Style.BRIGHT}")
        print("=" * 60)
        print("🤖 Mini GPT Assistant")
        print("=" * 60)
        print(f"{Style.RESET_ALL}")
        print(f"{Fore.WHITE}Welcome! I'm your local AI assistant.{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}Model: {config.MODEL_NAME}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}Internet: {'Enabled' if config.ALLOW_INTERNET else 'Disabled'}{Style.RESET_ALL}")
        print(f"{Fore.WHITE}Type 'quit', 'exit', or 'bye' to end the conversation.{Style.RESET_ALL}")
        print(f"{Fore.WHITE}Type 'clear' to clear conversation history.{Style.RESET_ALL}")
        print(f"{Fore.WHITE}Type 'help' for more commands.{Style.RESET_ALL}")
        print()
    
    def display_help(self):
        """Display help information."""
        print(f"{Fore.CYAN}Available Commands:{Style.RESET_ALL}")
        print(f"{Fore.WHITE}  help     - Show this help message{Style.RESET_ALL}")
        print(f"{Fore.WHITE}  clear    - Clear conversation history{Style.RESET_ALL}")
        print(f"{Fore.WHITE}  history  - Show conversation history{Style.RESET_ALL}")
        print(f"{Fore.WHITE}  status   - Show assistant status{Style.RESET_ALL}")
        print(f"{Fore.WHITE}  quit/exit/bye - End the conversation{Style.RESET_ALL}")
        print()
    
    def display_history(self):
        """Display conversation history."""
        if not self.conversation_history:
            print(f"{Fore.YELLOW}No conversation history yet.{Style.RESET_ALL}")
            return
        
        print(f"{Fore.CYAN}Conversation History:{Style.RESET_ALL}")
        for i, exchange in enumerate(self.conversation_history, 1):
            print(f"{Fore.WHITE}{i}. Human: {exchange['user']}{Style.RESET_ALL}")
            print(f"{Fore.GREEN}   Assistant: {exchange['assistant']}{Style.RESET_ALL}")
            print()
    
    def display_status(self):
        """Display assistant status."""
        print(f"{Fore.CYAN}Assistant Status:{Style.RESET_ALL}")
        print(f"{Fore.WHITE}  Model: {config.MODEL_NAME}{Style.RESET_ALL}")
        print(f"{Fore.WHITE}  Device: {'GPU' if torch.cuda.is_available() else 'CPU'}{Style.RESET_ALL}")
        print(f"{Fore.WHITE}  Internet: {'Enabled' if config.ALLOW_INTERNET else 'Disabled'}{Style.RESET_ALL}")
        print(f"{Fore.WHITE}  Conversation exchanges: {len(self.conversation_history)}{Style.RESET_ALL}")
        print(f"{Fore.WHITE}  Log file: {config.LOG_FILE}{Style.RESET_ALL}")
        print()
    
    def clear_history(self):
        """Clear conversation history."""
        self.conversation_history.clear()
        print(f"{Fore.GREEN}Conversation history cleared.{Style.RESET_ALL}")
        self.logger.info("Conversation history cleared by user")
    
    def run(self):
        """Main conversation loop."""
        self.display_welcome()
        
        try:
            while True:
                # Get user input
                user_input = input(f"{Fore.BLUE}You: {Style.RESET_ALL}").strip()
                
                if not user_input:
                    continue
                
                # Handle commands
                if user_input.lower() in ['quit', 'exit', 'bye']:
                    print(f"{Fore.GREEN}Thank you for using Mini GPT Assistant! Goodbye!{Style.RESET_ALL}")
                    break
                elif user_input.lower() == 'help':
                    self.display_help()
                    continue
                elif user_input.lower() == 'clear':
                    self.clear_history()
                    continue
                elif user_input.lower() == 'history':
                    self.display_history()
                    continue
                elif user_input.lower() == 'status':
                    self.display_status()
                    continue
                
                # Generate and display response
                print(f"{Fore.GREEN}Assistant: {Style.RESET_ALL}", end="")
                response = self.generate_response(user_input)
                print(response)
                print()
                
                # Add to history
                self.add_to_history(user_input, response)
                
        except KeyboardInterrupt:
            print(f"\n{Fore.YELLOW}Conversation interrupted by user.{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.RED}An unexpected error occurred: {e}{Style.RESET_ALL}")
            self.logger.error(f"Unexpected error in main loop: {e}")


def main():
    """Main entry point."""
    try:
        assistant = MiniGPTAssistant()
        assistant.run()
    except Exception as e:
        print(f"{Fore.RED}Failed to start assistant: {e}{Style.RESET_ALL}")
        sys.exit(1)


if __name__ == "__main__":
    main()
