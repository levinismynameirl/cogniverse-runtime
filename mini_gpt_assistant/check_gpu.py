"""
GPU diagnostic script for Mini GPT Assistant.
Run this to check if your GPU is properly configured.
"""

import torch
import subprocess
import platform

def check_cuda():
    """Check CUDA availability and configuration."""
    print("🔍 GPU Diagnostic Check")
    print("=" * 50)
    
    # Check PyTorch CUDA support
    print(f"PyTorch version: {torch.__version__}")
    print(f"CUDA available: {torch.cuda.is_available()}")
    
    if torch.cuda.is_available():
        print(f"CUDA version: {torch.version.cuda}")
        print(f"cuDNN version: {torch.backends.cudnn.version()}")
        print(f"Number of GPUs: {torch.cuda.device_count()}")
        
        for i in range(torch.cuda.device_count()):
            gpu = torch.cuda.get_device_properties(i)
            memory_gb = gpu.total_memory / 1024**3
            print(f"GPU {i}: {gpu.name} ({memory_gb:.1f}GB)")
        
        # Test GPU memory allocation
        try:
            test_tensor = torch.randn(1000, 1000).cuda()
            print("✅ GPU memory allocation test passed")
            del test_tensor
            torch.cuda.empty_cache()
        except Exception as e:
            print(f"❌ GPU memory allocation test failed: {e}")
    else:
        print("❌ CUDA not available")
        print("\nPossible solutions:")
        print("1. Install CUDA-enabled PyTorch:")
        print("   pip uninstall torch torchvision torchaudio")
        print("   pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118")
        print("2. Check if NVIDIA drivers are installed")
        print("3. Verify GPU compatibility with CUDA")

def check_nvidia_gpu():
    """Check NVIDIA GPU using nvidia-smi."""
    try:
        result = subprocess.run(['nvidia-smi'], capture_output=True, text=True)
        if result.returncode == 0:
            print("\n📊 NVIDIA GPU Status:")
            print(result.stdout)
        else:
            print("❌ nvidia-smi not found or failed")
    except FileNotFoundError:
        print("❌ nvidia-smi command not found")
        print("Install NVIDIA drivers from https://www.nvidia.com/drivers/")

if __name__ == "__main__":
    check_cuda()
    check_nvidia_gpu()