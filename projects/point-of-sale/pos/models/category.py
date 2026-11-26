from database import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, ForeignKey,String

class Category(Base):
    
    __tablename__= "categories"
    
    category_id=Column(Integer, primary_key=True, index=True)
    product_id=Column(Integer, ForeignKey("products.product_id"), nullable=False)
    category_name=Column(String,nullable=False)
    

    product=relationship("Product", back_populates="category")

    
    