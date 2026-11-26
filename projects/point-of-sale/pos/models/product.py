from database import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Float

class Product(Base):
    
    __tablename__= "products"
    
    product_id=Column(Integer, primary_key=True, index=True)
    product_name=Column(String,nullable=False, index=True)
    sku=Column(String,nullable=False)
    barcode=Column(String,nullable=False)
    cost_price=Column(Float,nullable=False, index=True)
    selling_price=Column(Float,nullable=False, index=True)
    
    suppliers=relationship("Supplier", back_populates="product")
    category=relationship("Category", back_populates="product")

    
    