from database import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer

class  User(Base):
    
    __tablename__= "users"
    
    user_id=Column(Integer, primary_key=True, index=True)
    username=Column(nullable=False)
    password_hash=Column(nullable=False)
    role=Column(nullable=False)
    email=Column(nullable=False)
    created_at=Column(nullable=False)
    is_active=Column(nullable=False)

    order=relationship("Order", back_populates="user")