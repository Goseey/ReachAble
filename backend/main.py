from fastapi import FastAPI
import httpx

endpoints = []

def check_endpoint(url: str) -> bool:
    try:
        response = httpx.get(url, timeout=5)
        return response.status_code < 400
    except:
        return False

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/check")
def check(url: str):
    result = check_endpoint(url)

    return {
        "url": url,
        "is_up": result
    }

@app.post("/endpoints")
def add_endpoint(name: str, url: str):
    endpoint = {
        "id": len(endpoints) + 1,
        "name": name,
        "url": url
    }

    endpoints.append(endpoint)

    return endpoint

@app.get("/endpoints")
def get_endpoints():
    return endpoints

@app.delete("/endpoints/{endpoint_id}")
def delete_endpoint(endpoint_id: int):
    global endpoints

    endpoints = [e for e in endpoints if e["id"] != endpoint_id]

    return {"message": "deleted"}from fastapi import FastAPI
import httpx

endpoints = []

def check_endpoint(url: str) -> bool:
    try:
        response = httpx.get(url, timeout=5)
        return response.status_code < 400
    except:
        return False

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/check")
def check(url: str):
    result = check_endpoint(url)

    return {
        "url": url,
        "is_up": result
    }

@app.post("/endpoints")
def add_endpoint(name: str, url: str):
    endpoint = {
        "id": len(endpoints) + 1,
        "name": name,
        "url": url
    }

    endpoints.append(endpoint)

    return endpoint

@app.get("/endpoints")
def get_endpoints():
    return endpoints

@app.delete("/endpoints/{endpoint_id}")
def delete_endpoint(endpoint_id: int):
    global endpoints

    endpoints = [e for e in endpoints if e["id"] != endpoint_id]

    return {"message": "deleted"}
