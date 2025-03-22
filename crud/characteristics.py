from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

import models
import schemas

async def create_characteristic(
        db: AsyncSession,
        characteristic: schemas.CharacteristicCreate,
        product_id: int
):
    db_characteristic = models.Characteristic(
        name=characteristic.name,
        value=characteristic.value,
        product_id=product_id
    )
    db.add(db_characteristic)
    await db.commit()
    await db.refresh(db_characteristic)
    return db_characteristic

async def get_characteristics(db: AsyncSession, product_id: int):
    result = await db.execute(
        select(models.Characteristic).filter(models.Characteristic.product_id == product_id)
    )
    return result.scalars().all()

async def update_characteristic(
        db: AsyncSession,
        characteristic_id: int,
        characteristic: schemas.CharacteristicCreate
):
    db_characteristic = await db.get(models.Characteristic, characteristic_id)
    if db_characteristic:
        db_characteristic.name = characteristic.name
        db_characteristic.value = characteristic.value
        await db.commit()
        return db_characteristic
    return None

async def delete_characteristic(db: AsyncSession, characteristic_id: int):
    db_characteristic = await db.get(models.Characteristic, characteristic_id)
    if db_characteristic:
        await db.delete(db_characteristic)
        await db.commit()
        return db_characteristic
    return None
