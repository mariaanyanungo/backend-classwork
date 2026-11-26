from pos.schemas.supplier import SupplierRead, SupplierCreate
from fastapi import  HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from database import get_db
from pos.repositories.supplier import SupplierRepository

router=APIRouter(prefix="/suppliers", tags=["suppliers"])

@router.get("/", response_model=list[SupplierRead])
def read_suppliers(db:Session=Depends(get_db)):
    db_supplier=SupplierRepository.get_suppliers(db)
    if db_supplier is None:
        raise HTTPException (status_code=404, detail="supplier not found")
    return db_supplier

@router.get("/{supplier_id}", response_model=SupplierRead)
def read_supplier(db:Session=Depends(get_db)):
    db_supplier=SupplierRepository.get_supplier(db)
    if db_supplier is None:
        raise HTTPException (status_code=404, detail="supplier not found")
    return db_supplier


@router.post("/{supplier_id}", response_model=SupplierCreate)
def make_supplier(supplier:SupplierCreate, db:Session=Depends(get_db)):
    db_supplier=SupplierRepository.create_supplier(db, supplier)
    return db_supplier

@router.delete("/{supplier_id}")
def remove_supplier(db:Session=Depends(get_db)):
    db_supplier=SupplierRepository.delete_supplier(db)
    if not db_supplier:
     raise HTTPException(status_code=404, detail="supplier not found")
    return {"detail": "supplier successfully deleted"}
  
    


    
    
    
    