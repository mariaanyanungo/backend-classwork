from sqlalchemy.orm import Session
from datetime import datetime, date, time
from decimal import Decimal
from ttt_backend.models.coins import Coins
from sqlalchemy import and_
import uuid

class coinsRepository:
    
    def __init__(self):
        self.model = Coins
        
    def get_coin_by_id(self, db: Session, id: int):
        return db.query(Coins).filter(Coins.id == id).all() 
    
    def get_coin_by_teacher_id(self, db: Session, teacher_id: uuid.UUID):
        return db.query(Coins).filter(Coins.teacher_id == teacher_id).all() 
    
    def get_coin_by_job_id(self, db: Session, job_id: uuid.UUID):
        return db.query(Coin).filter(Coin.job_id == job_id).all() 
    
    def get_coin_by_payment_id(self, db: Session, payment_id: uuid.UUID):
        return db.query(Coins).filter(Coins.payment_id == payment_id).all() 
    
    def create_coin_record(self, db: Session, data: dict):
        coin = Coins(**data)
        db.add(coin)
        db.commit()
        db.refresh(coin)
        return coin
        
    def update_coins(self, db: Session, db_obj: Coins, data: dict):
        for field, value in data.items():
            setattr(db_obj, field, value)
        db.commit()
        db.refresh(db_obj)
        return db_obj
        
    def delete_coin_record(self, db: Session, db_obj: Coins) -> None:
        db.delete(db_obj)
        db.commit()
