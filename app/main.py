from fastapi import FastAPI

app = FastAPI(title="Perception Data Platform")

@app.get("/")
def read_root():
    return {"status": "ok", "message": "Perception data platform is running"}