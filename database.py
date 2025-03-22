import ssl
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

ssl_context = ssl.create_default_context(cafile="/Users/macbook/Desktop/eu-central-1-bundle.pem")

DATABASE_URL = "postgresql+asyncpg://fastapi_user:lolkek17@fastapi-db.cdiy4my8iw6o.eu-central-1.rds.amazonaws.com:5432/fastapi-db"

engine = create_async_engine(DATABASE_URL, connect_args={"ssl": ssl_context})

SessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

async def get_db():
    async with SessionLocal() as session:
        yield session
