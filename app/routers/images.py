from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import Optional

from app.database import get_db
from app.db_models.core import Image, Dataset
from app.schemas.image import ImageResponse, IngestResult
from app.services.ingestion import ingest_folder

router = APIRouter(tags=["images"])

@router.post("/datasets/{dataset_id}/ingest", response_model=IngestResult)
def ingest_images(dataset_id: int, folder_path: str, db: Session = Depends(get_db)):
    dataset = db.query(Dataset).filter(Dataset.id == dataset_id).first()
    if not dataset:
        raise HTTPException(status_code=404, detail="Dataset not found")

    ingested, skipped = ingest_folder(folder_path, dataset_id, db)
    return IngestResult(ingested=ingested, skipped=skipped, dataset_id=dataset_id)

@router.get("/images/", response_model=list[ImageResponse])
def list_images(
    status: Optional[str] = None,
    split: Optional[str] = None,
    skip: int = 0,
    limit: int = Query(default=50, le=200),
    db: Session = Depends(get_db),
):
    query = db.query(Image)
    if status:
        query = query.filter(Image.status == status)
    if split:
        query = query.filter(Image.split == split)
    return query.offset(skip).limit(limit).all()