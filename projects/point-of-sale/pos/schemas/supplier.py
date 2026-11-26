from pydantic import BaseModel

class SupplierBase(BaseModel):
    supplier_id:int
    product_id:int
    supplier_name:str
    phone_number:str
    barcode:str
    address:str
    created_at:str
     
class SupplierCreate(SupplierBase):
    pass

class SupplierRead(SupplierBase):
    pass

class SupplierUpdate(SupplierBase):
    phone_number:str
    address:str
    
class SupplierDelete(BaseModel):
    supplier_id:int
    
    class Config:
        orm_mode=True
    

    
    
    
    