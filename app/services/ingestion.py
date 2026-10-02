import os
from PIL import Image as PILImage
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from app.db_models.core import Image

SUPPORTED_EXTENSIONS = (".jpg", ".jpeg", ".png")

def ingest_folder(folder_path: str, dataset_id: int, db: Session) -> tuple[int, int]:
    ingested = 0
    skipped = 0

    for file_name in sorted(os.listdir(folder_path)):
        if not file_name.lower().endswith(SUPPORTED_EXTENSIONS):
            continue

        full_path = os.path.join(folder_path, file_name)

        try:
            with PILImage.open(full_path) as img:
                width, height = img.size
        except Exception:
            skipped += 1
            continue

        image = Image(
            dataset_id=dataset_id,
            file_name=file_name,
            file_path=full_path,
            width=width,
            height=height,
        )
        db.add(image)
        try:
            db.commit()
            ingested += 1
        except IntegrityError:
            db.rollback()
            skipped += 1

    return ingested, skipped