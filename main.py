from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

import crud.products as product_crud
import crud.characteristics as characteristic_crud

import models
import schemas
import database
from database import get_db
from models import Product

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to the FastApi project"}


@app.on_event("startup")
async def on_startup():
    async with database.engine.begin() as conn:
        await conn.run_sync(database.Base.metadata.create_all)

@app.get("/products/", response_model=list[schemas.Product])
async def get_products(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(database.get_db)):
    return await product_crud.get_products(db=db, skip=skip, limit=limit)

@app.post("/products/", response_model=schemas.Product)
async def create_product(product: schemas.ProductCreate, db: AsyncSession = Depends(database.get_db)):
    return await product_crud.create_product(db=db, product=product)

@app.get("/products/{product_id}", response_model=schemas.Product)
async def get_product(product_id: int, db: AsyncSession = Depends(database.get_db)):
    db_product = await product_crud.get_product(db=db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product

@app.put("/products/{product_id}", response_model=schemas.Product)
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

@app.delete("/products/{product_id}", response_model=schemas.Product)
async def delete_product(
        product_id: int,
        db: AsyncSession = Depends(database.get_db)
):
    db_product = await product_crud.delete_product(db=db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product

@app.post("/characteristics/{product_id}", response_model=schemas.Characteristic)
async def create_characteristic(
        product_id: int,
        characteristic: schemas.CharacteristicCreate,
        db: AsyncSession = Depends(database.get_db)):
    return await characteristic_crud.create_characteristic(db=db, characteristic=characteristic, product_id=product_id)

@app.get("/characteristics/{product_id}", response_model=list[schemas.Characteristic])
async def get_characteristics(product_id: int, db: AsyncSession = Depends(database.get_db)):
    return await characteristic_crud.get_characteristics(db=db, product_id=product_id)

@app.put("/characteristics/{characteristic_id}", response_model=schemas.Characteristic)
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

@app.delete("/characteristics/{characteristic_id}", response_model=schemas.Characteristic)
async def delete_characteristic(
        characteristic_id: int,
        db: AsyncSession = Depends(database.get_db)
):
    db_characteristic = await characteristic_crud.delete_characteristic(db=db, characteristic_id=characteristic_id)
    if db_characteristic is None:
        raise HTTPException(status_code=404, detail="Characteristic not found")
    return db_characteristic
