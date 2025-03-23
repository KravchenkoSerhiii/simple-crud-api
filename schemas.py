from pydantic import BaseModel, Field
from typing import List, Optional

class CharacteristicBase(BaseModel):
    name: str = Field(
        ...,
        title="Name of characteristic",
        description="Colour or weight",
        example="Colour"
    )
    value: str = Field(
        ...,
        title="Value of characteristic",
        description="Black, white, etc",
        example="Black"
    )

class CharacteristicCreate(CharacteristicBase):
    pass

class Characteristic(CharacteristicBase):
    id: int = Field(
        ...,
        title="ID of characteristic",
        example=2
    )
    product_id: int = Field(
        ...,
        title="ID of required product",
        example=1
    )

    class Config:
        orm_mode = True

class ProductBase(BaseModel):
    name: str = Field(
        ...,
        title="Name of product",
        description="Name of requiered product",
        example="Laptop"
    )
    quantity: int = Field(
        ...,
        title="Quantity of product",
        description="How much of this product we have",
        example=30
    )
    sku: str = Field(
        ...,
        title="SKU of product",
        description="Unique identifier for this product",
        example="LAP712"
    )

class ProductCreate(ProductBase):
    name: str
    quantity: int
    sku: str
    # characteristics: List[CharacteristicCreate] = Field(
    #     default=[], title="Characteristics of product",
    #     description="Additional info about product",
    #     example="RAM"
    # )

class Product(ProductBase):
    id: int = Field(..., title="ID of product", description="Unique identifier for this product")
    name: str = Field(
        ...,
        title="Name of product",
        description="Name of requiered product",
        example="Laptop",
    )
    quantity: int = Field(
        ...,
        title="Quantity of product",
        description="How much of this product we have",
        example=30
    )
    sku: str = Field(
        ...,
        title="SKU of product",
        description="Unique identifier for this product",
        example="LAP223"
    )
    # characteristics: List[Characteristic] = Field(
    #     default=[], title="Characteristics of product",
    #     description="Additional info about product",
    #     example=1
    # )

    class Config:
        orm_mode = True
