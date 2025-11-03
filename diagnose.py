#!/usr/bin/env python3
import sys
import os
import subprocess

print("=== Python Interpreter ===")
print(f"sys.executable: {sys.executable}")
print(f"sys.version: {sys.version}")
print(f"sys.prefix: {sys.prefix}")
print()

print("=== Python Path ===")
for p in sys.path:
    print(f"  {p}")
print()

print("=== Environment Variables ===")
print(f"VIRTUAL_ENV: {os.environ.get('VIRTUAL_ENV', 'NOT SET')}")
print(f"PATH: {os.environ.get('PATH', 'NOT SET')[:200]}...")
print()

print("=== Can import torch? ===")
try:
    import torch
    print(f"✓ torch imported successfully")
    print(f"  torch version: {torch.__version__}")
    print(f"  torch location: {torch.__file__}")
except ImportError as e:
    print(f"✗ Cannot import torch: {e}")
print()

print("=== Venv Python Check ===")
venv_python = "/workspace/LLMs-from-scratch/.venv/bin/python"
if os.path.exists(venv_python):
    result = subprocess.run([venv_python, "-c", "import torch; print(torch.__version__)"],
                          capture_output=True, text=True)
    if result.returncode == 0:
        print(f"✓ Venv Python CAN import torch: {result.stdout.strip()}")
    else:
        print(f"✗ Venv Python CANNOT import torch: {result.stderr}")
else:
    print(f"✗ Venv Python not found at {venv_python}")
print()

print("=== Jupyter Kernels ===")
result = subprocess.run(["jupyter", "kernelspec", "list"], capture_output=True, text=True)
print(result.stdout)
