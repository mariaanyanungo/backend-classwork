import uuid
from sqlalchemy import Column, Integer, DateTime, ForeignKey
import uuid
from database import Base
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

class Coins(Base):
    __tablename__ = "coins"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    teacher_id = Column(UUID(as_uuid=True), ForeignKey("users.user_id"), nullable=False, index=True)
    # job_id = Column(UUID(as_uuid=True), ForeignKey("jobs_posted.job_id"), nullable=False, index=True)
    # payment_id = Column(UUID(as_uuid=True), ForeignKey("payments.payment_id"), nullable=False, index=True)
    coins = Column(Integer, nullable=False, default=0, index=True)
    coins_used = Column(Integer, nullable=False, default=0, index=True)
    coins_remaining = Column(Integer, nullable=False, default=0, index=True)
    created_at = Column(DateTime, index=True, nullable=False)
    updated_at = Column(DateTime, index=True, nullable=False)
    
    # user=relationship("User", back_populates="coins")
    # user=relationship("User", back_populates="jobs_posted")
    # user=relationship("User", back_populates="payments")
    
