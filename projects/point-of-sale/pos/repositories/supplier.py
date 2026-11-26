from sqlalchemy.orm import Session
from pos.models.supplier import Supplier


class SupplierRepository:
    def get_supplier(db:Session):
        return db.query(Supplier).filter(Supplier.supplier_id==Supplier.supplier_id).first()
    
    def get_suppliers(db:Session, skip: int=0, limit: int=100):
        return db.query(Supplier).offset(skip).limit(limit).all()
    
  
    def create_supplier(db:Session, supplier):
        db_supplier=supplier(**supplier.model_dump())
        db.add(db_supplier)
        db.commit()
        db.refresh(db_supplier)
        return db_supplier
    
    def delete_supplier(db:Session):
        return

