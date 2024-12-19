from typing import Annotated
from fastapi import Depends
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import declarative_base, Session

url_object = URL.create(
  "postgresql+psycopg2",
  username="postgres",
  password="1234",
  host="localhost",
  port="5433",
  database="ecommerce"
)

engine = create_engine(url_object)

Base = declarative_base()

def create_db_and_tables():
  Base.metadata.create_all(bind= engine)
  
def get_session():
  with Session(engine) as session:
    yield session
    
SessionDep = Annotated[Session, Depends(get_session)]