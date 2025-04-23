from app.handler.endpoints import records_router
from fastapi import FastAPI

from dotenv import load_dotenv

load_dotenv()

app = FastAPI()
app.include_router(records_router)
