from datetime import datetime
from typing import Optional
from uuid import UUID
from pydantic import BaseModel


class RecordCreateResponse(BaseModel):
    id: UUID


class RecordReadResponse(BaseModel):
    content: str

class RecordListItem(BaseModel):
    id: UUID
    name: str
    created_at: datetime
    marked: bool


class RecordMarkResponse(BaseModel):
    flag: bool