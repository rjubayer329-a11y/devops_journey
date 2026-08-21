#i/bin/bash
cd /home/jubayer/devops_journey
echo "=== Starting Pipeline: $(date) ==="
/usr/bin/python3 health_check.py
/usr/bin/python3 parse_logs.py
echo "=== Pipeline Completed ==="