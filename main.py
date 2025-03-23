from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

import crud.products as product_crud
import crud.characteristics as characteristic_crud

import models
import schemas
import database
from database import get_db
from models import Product

app = FastAPI(
    title="Products API",
    description="Api for managing products and characteristics",
    version="1.0",
)

@app.get("/")
async def root():
    return {"message": "Welcome to the FastApi project"}


@app.on_event("startup")
async def on_startup():
    async with database.engine.begin() as conn:
        await conn.run_sync(database.Base.metadata.create_all)

@app.get("/products/",
         response_model=list[schemas.Product],
         summary="Get all products",
         description="Return list of all products in DB",
         responses={200: {"description": "List of all products"}},
         )
async def get_products(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(database.get_db)):
    return await product_crud.get_products(db=db, skip=skip, limit=limit)

@app.post("/products/",
          response_model=schemas.Product,
          summary="Create a new product",
          description="Create a new product in DB",
          responses={
              200: {"description": "Product created"},
              400: {"description": "Invalid data"},
          }
          )
async def create_product(product: schemas.ProductCreate, db: AsyncSession = Depends(database.get_db)):
    return await product_crud.create_product(db=db, product=product)

@app.get("/products/{product_id}",
         response_model=schemas.Product,
         summary="Get a product by ID",
         description="Get required product by ID",
         responses={
             200: {"description": "Product found"},
             400: {"description": "Invalid data"},
         }
         )
async def get_product(product_id: int, db: AsyncSession = Depends(database.get_db)):
    db_product = await product_crud.get_product(db=db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product

@app.put("/products/{product_id}",
         response_model=schemas.Product,
         summary="Update a product",
         description="Update a product in DB by ID",
         responses={200: {"description": "Product updated"},
                    400: {"description": "Invalid data"},}
         )
async def update_product(
        product_id: int,
        product: schemas.ProductCreate,
        db: AsyncSession = Depends(database.get_db)
):
    db_product = await product_crud.update_product(
        db=db,
        product_id=product_id,
        product=product
    )
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product

@app.delete("/products/{product_id}",
            response_model=schemas.Product,
            summary="Delete a product",
            description="Delete a product in DB by ID",
            responses={
                200: {"description": "Product deleted"},
            }
            )
async def delete_product(
        product_id: int,
        db: AsyncSession = Depends(database.get_db)
):
    db_product = await product_crud.delete_product(db=db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product

@app.post("/characteristics/{product_id}",
          response_model=schemas.Characteristic,
          summary="Update a characteristic",
          description="Update a characteristic of product in DB by ID",
          responses={200: {"description": "Character updated"},
                     400: {"description": "Invalid data"},
                     }
          )
async def create_characteristic(
        product_id: int,
        characteristic: schemas.CharacteristicCreate,
        db: AsyncSession = Depends(database.get_db)):
    return await characteristic_crud.create_characteristic(db=db, characteristic=characteristic, product_id=product_id)

@app.get("/characteristics/{product_id}",
         response_model=list[schemas.Characteristic],
         summary="Get all characteristics",
         description="Return list of all characteristics in DB",
         responses={200: {"description": "List of all characteristics"}},
         )
async def get_characteristics(product_id: int, db: AsyncSession = Depends(database.get_db)):
    return await characteristic_crud.get_characteristics(db=db, product_id=product_id)

@app.put("/characteristics/{characteristic_id}",
         response_model=schemas.Characteristic,
         summary="Update a characteristic",
         description="Update a characteristic in DB by ID",
         responses={200: {"description": "Characteristic updated"},}
         )
async def update_characteristic(
        characteristic_id: int,
        characteristic: schemas.CharacteristicCreate,
        db: AsyncSession = Depends(database.get_db)
):
    db_characteristic = await characteristic_crud.update_characteristic(
        db=db,
        characteristic_id=characteristic_id,
        characteristic=characteristic
    )
    if db_characteristic is None:
        raise HTTPException(status_code=404, detail="Characteristic not found")
    return db_characteristic

@app.delete("/characteristics/{characteristic_id}",
            response_model=schemas.Characteristic,
            summary="Delete a characteristic",
            description="Delete a characteristic in DB by ID",
            responses={200: {"description": "Character deleted"},}
            )
async def delete_characteristic(
        characteristic_id: int,
        db: AsyncSession = Depends(database.get_db)
):
    db_characteristic = await characteristic_crud.delete_characteristic(db=db, characteristic_id=characteristic_id)
    if db_characteristic is None:
        raise HTTPException(status_code=404, detail="Characteristic not found")
    return db_characteristic
