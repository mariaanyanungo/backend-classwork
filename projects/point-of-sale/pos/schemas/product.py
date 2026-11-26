from pydantic import BaseModel

class ProductBase(BaseModel):
    product_id:int
    product_name:str
    sku:str
    barcode:str
    cost_price:float
    selling_price:float
     
class ProductCreate(ProductBase):
    pass

class ProductRead(ProductBase):
    pass

class ProductUpdate(ProductBase):
    sku:str
    selling_price:float
    
class ProductDelete(BaseModel):
    product_id:int
    
    class Config:
        orm_mode=True
    

    
    
    
    