from sqlalchemy.orm import Session
from pos.models.order import Order


class orderRepository:
    def get_order(db:Session):
        return db.query(Order).filter(Order.order_id==Order.order_id).first()
    
    def get_orders(db:Session, skip: int=0, limit: int=100):
        return db.query(Order).offset(skip).limit(limit).all()
    
  
    def create_order(db:Session, order):
        db_order=order(**order.model_dump())
        db.add(db_order)
        db.commit()
        db.refresh(db_order)
        return db_order
    
    def delete_order(db:Session):
        return

