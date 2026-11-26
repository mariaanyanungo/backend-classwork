from database import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, ForeignKey

class  Payment(Base):
    
    __tablename__= "payment"
    
    sale_id=Column(Integer, primary_key=True, index=True)

    payment=relationship("Payment", back_populates="sale")

    
    