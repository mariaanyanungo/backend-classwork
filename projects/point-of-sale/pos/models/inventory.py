from database import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, ForeignKey

class Inventory(Base):
    
    __tablename__= "inventories"
    
    inventory_id=Column(Integer, primary_key=True, index=True)
    product_id=Column(ForeignKey("product_id"), nullable=False)
    quantity=Column(Integer, nullable=True)
    
    product=relationship("Product", back_populates="inventory")

    
    