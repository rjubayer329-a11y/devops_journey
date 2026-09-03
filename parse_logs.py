import json

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
                line = line.strip()
                if not line:
                    continue

                parts = line.split(" - ")
                if len(parts) < 2:
                    continue

                status_info = parts[1].split()
                status_code = status_info[0]
                self.total_checks += 1

                if status_code == "200":
                    self.up_count += 1
                elif status_code == "404":
                    self.failed_count += 1
                else:
                    self.down_count += 1
                    self.status_code[status_code] = self.status_code.get(status_code, 0) + 1
    def get_uptime_percentage(self):
        if self.total_checks == 0:
            return 0
        self.calculation = round((self.up_count / self.total_checks) * 100, 2)
        return f"{self.calculation}%"

    def get_alert_status(self, threshold):
        if self.calculation < threshold:
            return {
                "status": "CRITICAL",
                "message": f"Uptime dropped below {threshold}% threshold!"
            }
        else:
            return {
                "status": "OK",
                "message": "Uptime is within optimal parameters."
            }
with open("config.json", "r") as config_file:
    config = json.load(config_file)
analyzer = LogAnalyzer()
analyzer.open_file(config["log_file"])
summary = {
    "total_checks": analyzer.total_checks,
    "up": analyzer.up_count,
    "down": analyzer.down_count,
    "failed": analyzer.failed_count,
    "uptime_percentage": analyzer.get_uptime_percentage(),
    "alert": analyzer.get_alert_status(config["minimum_uptime"]),
    "http_error_breakdown": analyzer.status_code
}
print(json.dumps(summary, indent=4))