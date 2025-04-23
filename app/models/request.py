from datetime import datetime
from typing import Optional
from uuid import UUID
from pydantic import BaseModel

class RecordCreateRequest(BaseModel):
    name: str
    content: Optional[str] = None

class RecordUpdateRequest(BaseModel):
    id: UUID
    content: Optional[str] = None

class RecordDeleteRequest(BaseModel):
    id: UUID

class RecordReadRequest(BaseModel):
    id: UUID

class RecordListItem(BaseModel):
    id: UUID
    name: str
    created_at: datetime
    marked: bool

class RecordMarkRequest(BaseModel):
    id: UUID
