from fastapi import HTTPException, status
from sqlalchemy import select
from app.internal.model.product import Product

def get_list(session, offset, limit):
  stmt = select(Product).offset(offset).limit(limit)
  products = session.execute(stmt).scalars().all()
  return products

def get_detail(id, session):
  product = session.get(Product, id)
  if product == None:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"product not found")
  return product

def create(product, session):
  new_product = Product(**product.model_dump())
  session.add(new_product)
  session.commit()
  session.refresh(new_product)
  return new_product

def updates(id, product, session):
  updated_product = session.query(Product).filter(Product.id == id)
  updated_product.first()
  if updated_product == None:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"product not found")
  else:
    updated_product.update(product.model_dump(), synchronize_session=False)
    session.commit()
  return updated_product.first()

def delete(id, session):
  product = session.get(Product, id)
  if product == None:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"product not found")
  session.delete(product)
  session.commit()
  return {"ok": True}