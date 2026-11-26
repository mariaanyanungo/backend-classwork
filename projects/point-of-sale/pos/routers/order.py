from pos.schemas.order import OrderRead, OrderCreate
from fastapi import  HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from database import get_db
from pos.repositories.order import orderRepository

router=APIRouter(prefix="/orders", tags=["orders"])

@router.get("/", response_model=list[OrderRead])
def read_orders(db:Session=Depends(get_db)):
    db_order=orderRepository.get_orders(db)
    if db_order is None:
        raise HTTPException (status_code=404, detail="order not found")
    return db_order

@router.get("/{order_id}", response_model=OrderRead)
def read_order(db:Session=Depends(get_db)):
    db_order=orderRepository.get_order(db)
    if db_order is None:
        raise HTTPException (status_code=404, detail="order not found")
    return db_order


@router.post("/{order_id}", response_model=OrderCreate)
def make_order(order:OrderCreate, db:Session=Depends(get_db)):
    db_order=orderRepository.create_order(db, order)
    return db_order

@router.delete("/{order_id}")
def remove_order(db:Session=Depends(get_db)):
    db_order=orderRepository.delete_order(db)
    if not db_order:
     raise HTTPException(status_code=404, detail="order not found")
    return {"detail": "order successfully deleted"}
  
    


    
    
    
    