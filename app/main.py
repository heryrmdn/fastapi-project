from itertools import product
from fastapi import FastAPI
from app.config.db import create_db_and_tables
from app.router.api_router import api_router

def lifespan(app: FastAPI):
  create_db_and_tables()
  yield

app = FastAPI(lifespan=lifespan)
app.include_router(api_router)