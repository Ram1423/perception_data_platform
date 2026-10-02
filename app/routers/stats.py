from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func

from app.database import get_db
from app.db_models.core import Image, Dataset

router = APIRouter(prefix="/stats", tags=["stats"])

@router.get("/progress")
def progress(dataset_id: int, db: Session = Depends(get_db)):
    dataset = db.query(Dataset).filter(Dataset.id == dataset_id).first()
    if not dataset:
        raise HTTPException(status_code=404, detail="Dataset not found")

    rows = (
        db.query(Image.status, func.count(Image.id))
        .filter(Image.dataset_id == dataset_id)
        .group_by(Image.status)
        .all()
    )

    counts = {status: count for status, count in rows}
    total = sum(counts.values())

    return {
        "dataset_id": dataset_id,
        "dataset_name": dataset.name,
        "total": total,
        "by_status": counts,
    }