from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload
import schemas

import models
import schemas

async def create_product(db: AsyncSession, product: schemas.ProductCreate):
    db_product = schemas.Product(name=product.name, quantity=product.quantity, sku=product.sku)
    db.add(db_product)
    await db.commit()
    await db.refresh(db_product)
    for characteristic in product.characteristics:
        db_characteristic = schemas.Characteristic(
            name=characteristic.name,
            value=characteristic.value,
            product_id=db_product.id,
        )
        db.add(db_characteristic)
    await db.commit()
    await db.refresh(db_product)
    return db_product

#Get all products
async def get_products(db: AsyncSession, skip: int = 0, limit: int = 100):
    result = await db.execute(
        select(models.Product)
        .offset(skip)
        .limit(limit)
        .options(selectinload(models.Product.characteristics))
    )
    return result.scalars().all()

# Get product with id
async def get_product(db: AsyncSession, product_id: int):
    result = await db.execute(
        select(models.Product)
        .filter(models.Product.id == product_id)
        .options(selectinload(models.Product.characteristics))
    )
    return result.scalar_one_or_none()

async def update_product(db: AsyncSession, product_id: int, product: schemas.ProductCreate):
    db_product = await get_product(db, product_id)
    if db_product:
        db_product.name = product.name
        db_product.quantity = product.quantity
        db_product.sku = product.sku
        await db.commit()
        return db_product
    return None

async def delete_product(db: AsyncSession, product_id: int):
    db_product = await get_product(db, product_id)
    if db_product:
        await db.delete(db_product)
        await db.commit()
        return db_product
    return None
