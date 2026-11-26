from pos.schemas.product import ProductRead, ProductCreate
from fastapi import  HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from database import get_db
from pos.repositories.product import ProductRepository

router=APIRouter(prefix="/products", tags=["products"])

@router.get("/", response_model=list[ProductRead])
def read_products(db:Session=Depends(get_db)):
    db_product=ProductRepository.get_products(db)
    if db_product is None:
        raise HTTPException (status_code=404, detail="product not found")
    return db_product

@router.get("/{product_id}", response_model=ProductRead)
def read_product(db:Session=Depends(get_db)):
    db_product=ProductRepository.get_product(db)
    if db_product is None:
        raise HTTPException (status_code=404, detail="product not found")
    return db_product


@router.post("/{product_id}", response_model=ProductCreate)
def make_product(product:ProductCreate, db:Session=Depends(get_db)):
    db_product=ProductRepository.create_product(db, product)
    return db_product

@router.delete("/{product_id}")
def remove_product(db:Session=Depends(get_db)):
    db_product=ProductRepository.delete_product(db)
    if not db_product:
     raise HTTPException(status_code=404, detail="Product not found")
    return {"detail": "Product successfully deleted"}
  
    


    
    
    
    