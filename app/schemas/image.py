from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional

class ImageResponse(BaseModel):
    id: int
    dataset_id: int
    file_name: str
    file_path: str
    width: Optional[int]
    height: Optional[int]
    split: str
    status: str
    created_at: datetime
    
    model_config = ConfigDict(from_attributes=True)

class IngestResult(BaseModel):
    ingested: int
    skipped: int
    dataset_id: int