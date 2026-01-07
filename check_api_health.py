import requests
import time

API_URL = "https://api.github.com"
TIMEOUT = 10

def check_api_health():
    start = time.time()
    try:
        response = requests.get(API_URL, timeout=TIMEOUT)
        latency = time.time() - start

        if response.status_code == 200:
            return {
                "status": "OK",
                "latency": round(latency, 3),
                "rate_limit": response.headers.get("X-RateLimit-Remaining")
            }
        else:
            return {
                "status": f"HTTP_{response.status_code}",
                "latency": round(latency, 3)
            }

    except requests.exceptions.Timeout:
        return {"status": "TIMEOUT"}
    except Exception as e:
        return {"status": "ERROR", "error": str(e)}

if __name__ == "__main__":
    result = check_api_health()
    print("API Health Check Result:")
    for k, v in result.items():
        print(f"{k}: {v}")
