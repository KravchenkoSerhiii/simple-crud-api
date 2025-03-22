from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    quantity = Column(Integer)
    sku = Column(String, unique=True)

    characteristics = relationship("Characteristic", back_populates="product")

    class Config:
        from_attributes = True


class Characteristic(Base):
    __tablename__ = "characteristics"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    value = Column(String)
    product_id = Column(Integer, ForeignKey("products.id"))

    product = relationship("Product", back_populates="characteristics")

    class Config:
        from_attributes = True
