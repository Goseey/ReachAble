import httpx
import models
from database import Base, engine, get_db
from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

Base.metadata.create_all(bind=engine)

app = FastAPI()


def check_endpoint(url: str) -> bool:
    try:
        response = httpx.get(url, timeout=5)
        return response.status_code < 400
    except:
        return False


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/check")
def check(url: str):
    result = check_endpoint(url)
    return {"url": url, "is_up": result}


@app.post("/endpoints")
def add_endpoint(name: str, url: str, db: Session = Depends(get_db)):
    endpoint = models.Endpoint(name=name, url=url)
    db.add(endpoint)
    db.commit()
    db.refresh(endpoint)
    return endpoint


@app.get("/endpoints")
def get_endpoints(db: Session = Depends(get_db)):
    return db.query(models.Endpoint).all()


@app.delete("/endpoints/{endpoint_id}")
def delete_endpoint(endpoint_id: int, db: Session = Depends(get_db)):
    endpoint = (
        db.query(models.Endpoint).filter(models.Endpoint.id == endpoint_id).first()
    )
    db.delete(endpoint)
    db.commit()
    return {"message": "deleted"}
