from app.internal.app.product.service import product_service

def get_list(session, offset, limit):
  products = product_service.get_list(session, offset, limit)
  return products

def get_detail(id, session):
  product = product_service.get_detail(id, session)
  return product

def create(product, session):
  new_product = product_service.create(product, session)
  return new_product

def updates(id, product, session):
  updated_product = product_service.updates(id, product, session)
  return updated_product

def delete(id, session):
  responses = product_service.delete(id, session)
  return responses