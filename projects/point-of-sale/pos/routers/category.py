from pos.schemas.category import CategoryRead, CategoryCreate
from fastapi import  HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from database import get_db
from pos.repositories.category import CategoryRepository

router=APIRouter(prefix="/categorys", tags=["categorys"])

@router.get("/", response_model=list[CategoryRead])
def read_categorys(db:Session=Depends(get_db)):
    db_category=CategoryRepository.get_categorys(db)
    if db_category is None:
        raise HTTPException (status_code=404, detail="category not found")
    return db_category

@router.get("/{category_id}", response_model=CategoryRead)
def read_category(db:Session=Depends(get_db)):
    db_category=CategoryRepository.get_category(db)
    if db_category is None:
        raise HTTPException (status_code=404, detail="category not found")
    return db_category


@router.post("/{category_id}", response_model=CategoryCreate)
def make_category(category:CategoryCreate, db:Session=Depends(get_db)):
    db_category=CategoryRepository.create_category(db, category)
    return db_category

@router.delete("/{category_id}")
def remove_category(db:Session=Depends(get_db)):
    db_category=CategoryRepository.delete_category(db)
    if not db_category:
     raise HTTPException(status_code=404, detail="category not found")
    return {"detail": "category successfully deleted"}
  
    


    
    
    
    