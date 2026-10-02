from fastapi import FastAPI
from app.database import Base, engine
from app.db_models import core  # noqa: F401 (needed so SQLAlchemy sees the models)

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Perception Data Platform")

@app.get("/")
def read_root():
    return {"status": "ok", "message": "Perception data platform is running"}