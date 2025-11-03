#!/bin/bash
set -e

echo "=== Installing IPython kernel for venv ==="
/workspace/LLMs-from-scratch/.venv/bin/python -m ipykernel install --user --name=llms-venv --display-name="Python (LLMs venv)"

echo ""
echo "=== Available kernels ==="
/workspace/LLMs-from-scratch/.venv/bin/jupyter kernelspec list

echo ""
echo "✓ Done! Now in Jupyter Lab:"
echo "  1. Go to Kernel -> Change Kernel"
echo "  2. Select 'Python (LLMs venv)'"
echo "  3. Restart the kernel"
