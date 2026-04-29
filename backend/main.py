from fastapi import FastAPI

app = FastAPI()

import httpx

def check_endpoint(url: str) -> dict:
    try:
        response = httpx.get(url, timeout=10)
        return {
            "url": url,
            "reachable": response.status_code == 200,
            "status_code": response.status_code,
            "response_time_ms": round(response.elapsed.total_seconds() * 1000),
        }
    except httpx.TimeoutException:
        return {"url": url, "reachable": False, "error": "Timeout"}
    except httpx.RequestError as e:
        return {"url": url, "reachable": False, "error": str(e)}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/check")
def check(url: str):
    result = check_endpoint(url)
    return result