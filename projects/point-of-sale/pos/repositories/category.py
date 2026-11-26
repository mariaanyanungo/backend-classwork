from sqlalchemy.orm import Session
from pos.models.category import Category

class CategoryRepository:
    def get_category(db:Session):
        return db.query(Category).filter(Category.category_id==Category.category_id).first()
    
    def get_categorys(db:Session, skip: int=0, limit: int=100):
        return db.query(Category).offset(skip).limit(limit).all()
    
  
    def create_category(db:Session, category):
        db_category=Category(**category.model_dump())
        db.add(db_category)
        db.commit()
        db.refresh(db_category)
        return db_category
    
    def delete_category(db:Session):
        return

