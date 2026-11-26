from database import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, ForeignKey

class  Payment(Base):
    
    __tablename__= "payments"
    
    payment_id=Column(Integer, primary_key=True, index=True)
    order_id=Column(Integer, ForeignKey("product_id"), nullable=False)
    payment_method=Column(nullable=False)
    amount=Column(nullable=False)
    payment_date=Column(nullable=False)
    created_at=Column(nullable=False)
    

    order=relationship("Order", back_populates="payment")

    
    