from fastapi import FastAPI
from src.settings import settings

app = FastAPI(title=settings.title)
