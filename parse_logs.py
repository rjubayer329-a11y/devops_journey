class log_analyzeselr:
    def __init__(self):
        self.error_count = 0

    def OpenFile(self, file_name):
        with open(file_name, "r") as file:
            for line in file:
                if "ERROR" in line or "WARNING" in line:
                    print(line)
                    self.error_count += 1
    def printError(self):
        print(f"Error found {self.error_count}")

analyzer = log_analyzeselr()
analyzer.OpenFile("server.log")
analyzer.printError()