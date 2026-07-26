import shutil


class SystemMonitor:

    def __init__(self, threshold_percent):
        self.threshold = threshold_percent

    def check_storage(self):
        # Gets disk usage for the root directory '/'
        total, used, free = shutil.disk_usage('/')

        # Calculate used percentage
        used_percent = (used / total) * 100

        print(f'Current Disk Usage: {used_percent:.2f}%')

        if used_percent > self.threshold:
            print('⚠️ WARNING: Disk space is running low!')
        else:
            print('✅ OK: Storage levels are healthy.')


# Create an instance checking for an 80% limit
monitor = SystemMonitor(threshold_percent=80)
monitor.check_storage()