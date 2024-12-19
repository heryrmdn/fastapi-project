from multiprocessing import synchronize
from typing import Annotated
from fastapi import APIRouter, HTTPException, Query, status
from sqlalchemy import select, update
from app.config.db import SessionDep
from app.internal.app.product.handler import product_handler
from app.internal.app.product.repository import product_repository
from app.internal.dto.product_dto import CreateProductRequest, UpdateProductRequest
from app.internal.model.product import Product

product_router = APIRouter()

@product_router.get("/product")
def get_list(session: SessionDep, offset: int = 0, limit: Annotated[int, Query(le=100)] = 100):
  products = product_handler.get_list(session, offset, limit)
  return products

@product_router.get("/product/{id}")
def get_detail(id: int, session: SessionDep):
  product = product_handler.get_detail(id, session)
  return product

@product_router.post("/product")
def create(product: CreateProductRequest, session: SessionDep):
  new_product = product_handler.create(product, session)
  return new_product

@product_router.put("/product/{id}")
def updates(id: int, product: UpdateProductRequest, session: SessionDep):
  updated_product = product_handler.updates(id, product, session)
  return updated_product

@product_router.delete("/product/{id}")
def delete(id: int, session: SessionDep):
  responses = product_handler.delete(id, session)
  return responses