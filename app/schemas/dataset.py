from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class DatasetCreate(BaseModel):
    name: str
    source_url: Optional[str] = None

class DatasetResponse(BaseModel):
    id: int
    name: str
    source_url: Optional[str]
    created_at: datetime

    class Config:
        from_attributes = True