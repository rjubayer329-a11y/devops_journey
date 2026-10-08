def summarize_error_count(log_file):
    error_count = {}
    with open(log_file) as file:
        for line in file:
            splitted_line = line.split(" - ")
            error_code = splitted_line[1].split(" ")[0]
            if error_code.startswith("4") or error_code.startswith("5"):
                error_count[error_code] = error_count.get(error_code, 0) + 1
    return error_count

if __name__ == "__main__":
    results = summarize_error_count("app.log")
    print("Error Summary:", results)