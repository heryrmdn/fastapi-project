from pydantic import BaseModel

class CreateProductRequest(BaseModel):
  title: str
  description: str
  at_sale: bool = False
  inventory: int
  
class UpdateProductRequest(BaseModel):
  title: str
  description: str
  at_sale: bool = False
  inventory: int