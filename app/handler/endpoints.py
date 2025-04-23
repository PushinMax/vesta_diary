from typing import List
from fastapi import APIRouter

from app.models.request import *
from app.models.response import *
from app.database.posgres import *


db = posgres()
records_router = APIRouter(prefix="/api/v1")

@records_router.post("/records/", response_model=RecordCreateResponse)
async def create_record(request: RecordCreateRequest):
    """
    Создание новой записи
    """
    id = db.create(request.name, request.content)
    return {"id": id}

@records_router.put("/records/")
async def update_record(request: RecordUpdateRequest):
    """
    Обновление содержимого записи
    """
    db.update(request.id, request.content)
    return {"success": True}

@records_router.delete("/records/")
async def delete_record(request: RecordDeleteRequest):
    """
    Удаление записи
    """
    db.delete(request.id)
    return {"success": True}

@records_router.post("/records/read", response_model=RecordReadResponse)
async def read_record(request: RecordReadRequest):
    """
    Чтение содержимого конкретной записи
    """
    content = db.read(request.id)
    return {"content": content}

@records_router.get("/records/list", response_model=List[RecordListItem])
async def show_list():
    """
    Получение списка всех записей
    """
    records = db.show_records()
    return [{
        "id": record[0],
        "name": record[1],
        "created_at": record[2],
        "marked": record[3]
    } for record in records]

@records_router.post("/records/mark", response_model=RecordMarkResponse)
async def mark_record(request: RecordMarkRequest):
    """
    Изменение флага marked записи
    """
    flag = db.mark(request.id)
    return {"flag": flag}