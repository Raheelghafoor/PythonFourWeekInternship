#!/bin/bash
echo "🧹 Running pylint..."
pylint my_module.py || exit 1

echo "✅ Running flake8..."
flake8 . --max-complexity 10 || exit 1

echo "📈 Running radon complexity..."
radon cc . -s

echo "📉 Compute maintainability..."
radon mi .