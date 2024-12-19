from app.internal.app.product.repository import product_repository

def get_list(session, offset, limit):
  products = product_repository.get_list(session, offset, limit)
  return products

def get_detail(id, session):
  product = product_repository.get_detail(id, session)
  return product

def create(product, session):
  new_product = product_repository.create(product, session)
  return new_product

def updates(id, product, session):
  updated_product = product_repository.updates(id, product, session)
  return updated_product

def delete(id, session):
  responses = product_repository.delete(id, session)
  return responses