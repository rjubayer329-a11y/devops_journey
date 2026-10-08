#!/bin/bash
TIMESTAMP=$(date +"%Y-%m-%d_%H-%M-%S")
REPORT_DIR="reports"
REPORT_FILE="${REPORT_DIR}/audit_${TIMESTAMP}.json"
echo "Running log audit check..."
mkdir -p "$REPORT_DIR"

if [ -f "app.log" ]; then
    echo "✅ Found 'app.log', now running 'audit_logs.py'"
    python3 audit_logs.py > "$REPORT_FILE"
    echo "✅Done! go to ${REPORT_FILE} to view the content"
    echo "Here is the file content:"
    cat "$REPORT_FILE"
else
    echo "⚠️ 'app.log' file not found!"
fi