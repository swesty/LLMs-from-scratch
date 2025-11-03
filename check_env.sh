#!/bin/bash
echo "=== Python paths ==="
which python
which python3
echo ""
echo "=== Venv Python ==="
ls -la .venv/bin/python* 2>&1 | head -5
echo ""
echo "=== Can we import torch? ==="
.venv/bin/python -c "import torch; print(f'torch version: {torch.__version__}')" 2>&1
echo ""
echo "=== Jupyter kernels ==="
.venv/bin/jupyter kernelspec list
