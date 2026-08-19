import json
import re
class LogAnalyzer:
    def __init__(self):
        self.total_checks = 0
        self.up_count = 0
        self.down_count = 0
        self.failed_count = 0
        self.status_code = {}

    def open_file(self, file_name):
        with open(file_name, "r") as file:
            for line in file:
                if "[UP]" in line:
                    self.up_count += 1
                elif "[DOWN]" in line:
                    self.down_count += 1
                    match = re.search(r"HTTP Error:\s*(\d+)", line)
                    if match:
                        code = match.group(1)
                        self.status_code[code] = self.status_code.get(code, 0) + 1
                elif "[FAILED]" in line:
                    self.failed_count += 1
                self.total_checks += 1
    def get_uptime_percentage(self):
        if self.total_checks == 0:
            return 0
        calculation = round((self.up_count / self.total_checks) * 100, 2)
        return f"{calculation}%"
analyzer = LogAnalyzer()
analyzer.open_file("health.log")
summary = {
    "total_checks": analyzer.total_checks,
    "up": analyzer.up_count,
    "down": analyzer.down_count,
    "failed": analyzer.failed_count,
    "uptime_percentage": analyzer.get_uptime_percentage(),
    "http_error_breakdown": analyzer.status_code
}
print(json.dumps(summary, indent=4))