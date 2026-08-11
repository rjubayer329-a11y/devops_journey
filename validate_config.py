import json
import os

config_file = "config.json"    #we can write here any json file we want to test
required_keys = ["app_name", "version", "environment", "port"]
Verify_existence = os.path.exists(config_file)


if Verify_existence == True:
    print("✅ File found!")
    with open(config_file, "r") as file:
        data = json.load(file)
        AppName = data.get("app_name")
        Port = data.get("port")
        confirmation = 0
        not_found_keys = []
        for key in required_keys:
            if key in data:
                confirmation = True
            elif key not in data:
                not_found_keys.append(key)
        

        if not_found_keys:
            print(f"Warning! the key {not_found_keys} is not found!")
        else:
            print(f"[OK] Configuration valid! App: {AppName} on port {Port}")

else:
    print("❌ File not found!")