import socket
import urllib.request
import urllib.error
import time

endpoints = [
    "https://httpbin.org/status/200",
    "https://httpbin.org/status/500",
    "https://httpbin.org/delay/1"
]


for link in endpoints:
    start_time = time.time()
    try:
        with urllib.request.urlopen(link, timeout=5) as response:
            end_time = time.time()
            duration = round((end_time - start_time)*1000, 2)
            print(
                f"✅ [UP] {link} - Status: {response.status} OK - Latency:"
                f"{duration}ms"
            )
    except urllib.error.HTTPError as e:
        print(f"❌ [DOWN] {link} - HTTP Error: {e.code}")
    except Exception as e:
        print(f"⚠️ [FAILED] {link} - Connection Error: {e}")