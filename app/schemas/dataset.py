from pydantic import BaseModel, ConfigDict
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
    
    model_config = ConfigDict(from_attributes=True)