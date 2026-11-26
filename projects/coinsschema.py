from __future__ import annotations
from pydantic import BaseModel, ConfigDict
import uuid
from datetime import datetime
from decimal import Decimal
from enum import Enum

class CoinsBase(BaseModel):
    # teacher_id: uuid.UUID
    # job_id: uuid.UUID
    # payment_id: uuid.UUID
    coins: int
    coins_used: int
    coins_remaining: int

class CoinsCreate(CoinsBase):
    pass

class CoinsUpdate(BaseModel):
    coins: int | None = None

class CoinsRead(CoinsBase):
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
