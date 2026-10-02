from fastapi import FastAPI
from app.database import Base, engine
from app.db_models import core  # noqa: F401
from app.routers import datasets, images

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Perception Data Platform")

app.include_router(datasets.router)
app.include_router(images.router)

@app.get("/")
def read_root():
    return {"status": "ok", "message": "Perception data platform is running"}