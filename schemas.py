from pydantic import BaseModel, Field
from typing import List, Optional

class CharacteristicBase(BaseModel):
    name: str = Field(..., title="Name of characteristic", description="Colour or weight")
    value: str = Field(..., title="Value of characteristic", description="Black, white, etc")

class CharacteristicCreate(CharacteristicBase):
    pass

class Characteristic(CharacteristicBase):
    id: int = Field(..., title="ID of characteristic")
    product_id: int = Field(..., title="ID of required product")

    class Config:
        orm_mode = True

class ProductBase(BaseModel):
    name: str = Field(..., title="Name of product", description="Example: Laptop, toy, car, etc")
    quantity: int = Field(..., title="Quantity of product", description="How much of this product we have")
    sku: str = Field(..., title="SKU of product", description="Unique identifier for this product")

class ProductCreate(ProductBase):
    characteristics: List[CharacteristicCreate] = Field(
        default=[], title="Characteristics of product",
        description="Additional info about product"
    )

class Product(ProductBase):
    id: int = Field(..., title="ID of product", description="Unique identifier for this product")
    characteristics: List[Characteristic] = Field(
        default=[], title="Characteristics of product",
        description="Additional info about product"
    )

    class Config:
        orm_mode = True
