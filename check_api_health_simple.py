#!/usr/bin/env python3
import urllib.request
import time
import json

API_URL = "https://api.github.com"
TIMEOUT = 10

def check_api_health():
    start = time.time()
    try:
        req = urllib.request.Request(API_URL, headers={'User-Agent': 'Python'})
        response = urllib.request.urlopen(req, timeout=TIMEOUT)
        latency = time.time() - start
        
        if response.status == 200:
            return {
                "status": "OK",
                "latency": round(latency, 3),
                "status_code": response.status
            }
        else:
            return {
                "status": f"HTTP_{response.status}",
                "latency": round(latency, 3)
            }
            
    except Exception as e:
        return {"status": "ERROR", "error": str(e)}

if __name__ == "__main__":
    result = check_api_health()
    print("API Health Check Result:")
    for k, v in result.items():
        print(f"{k}: {v}")
