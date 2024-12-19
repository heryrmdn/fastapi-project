from sqlalchemy import TIMESTAMP, Boolean, Column, Integer, String, text
from app.config.db import Base

class Product(Base):
  __tablename__= "products"
  
  id = Column(Integer, primary_key=True, nullable=False)
  title = Column(String)
  description = Column(String)
  at_sale = Column(Boolean)
  inventory = Column(Integer)
  added_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('Now()'))
  