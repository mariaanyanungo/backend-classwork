from pydantic import BaseModel

class OrderBase(BaseModel):
    order_id:int
    user_id:int
    status:str
    total_amount:float
    created_at:str
 
class OrderCreate(OrderBase):
    pass

class OrderRead(OrderBase):
    pass

class OrderUpdate(OrderBase):
    status:str
    total_amount:float
    
class OrderDelete(BaseModel):
    order_id:int
    
    class Config:
        orm_mode=True
    

    
    
    
    