from pydantic import BaseModel

class CategoryBase(BaseModel):
    category_id:int
    category_name:str
    product_id:int
     
class CategoryCreate(CategoryBase):
    pass

class CategoryRead(CategoryBase):
    pass

class CategoryUpdate(CategoryBase):
    category_name:int
    
class CategoryDelete(BaseModel):
    category_id:int
    
    class Config:
        orm_mode=True
    

    
    
    
    