import os
import shutil
from datetime import datetime

source_file = "server.log"
backup_dir = "backups"
os.makedirs(backup_dir, exist_ok=True)
current_date = datetime.now().strftime("%Y-%m-%d")
backup_path = f"{backup_dir}/server_backup_{current_date}.log"
shutil.copy(source_file, backup_path)
print(f"✅The file has backed up to the path: {backup_path} in the date {current_date}")