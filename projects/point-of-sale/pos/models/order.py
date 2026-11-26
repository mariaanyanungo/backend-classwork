from database import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, ForeignKey,String

class Order(Base):
    
    __tablename__= "orders"
    
    order_id=Column(Integer, primary_key=True, index=True)
    user_id=Column(Integer, ForeignKey("products.product_id"), nullable=False)
    status=Column(String,nullable=False)
    total_amount=Column(String,nullable=False)
    created_at=Column(String,nullable=False)
    
    user=relationship("User", back_populates="order")
    payment=relationship("Payment", back_populates="payment")
    

    
    