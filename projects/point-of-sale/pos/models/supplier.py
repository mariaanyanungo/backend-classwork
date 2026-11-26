from database import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, ForeignKey, String

class Supplier(Base):
    
    __tablename__="suppliers"
    
    supplier_id=Column(Integer, primary_key=True, index=True)
    product_id=Column(Integer, ForeignKey("products.product_id"))
    phone_number=Column(String, nullable=False)
    email=Column(String,nullable=False)
    address=Column(String,nullable=False)
    supplier_name=Column(String, nullable=False, index=True)
    created_at=Column(String,nullable=False)
    
    product=relationship("Product", back_populates="suppliers")