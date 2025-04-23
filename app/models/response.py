from datetime import datetime
from typing import Optional
from uuid import UUID
from pydantic import BaseModel


class RecordCreateResponse(BaseModel):
    id: UUID


class RecordReadResponse(BaseModel):
    content: str


class RecordMarkResponse(BaseModel):
    flag: bool