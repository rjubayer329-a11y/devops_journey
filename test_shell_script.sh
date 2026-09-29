#!/bin/bash
echo "Running log audit check..."
if [ -f "app.log" ]; then
    echo "✅ Found 'app.log', now running 'audit_logs.py'"
    python3 audit_logs.py
else
    echo "⚠️ 'app.log' file not found!"
fi