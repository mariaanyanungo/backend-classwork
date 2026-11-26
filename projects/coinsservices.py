from sqlalchemy.orm import Session
from ttt_backend.repositories.coinsrep import coinsRepository
from fastapi import HTTPException, status
from ttt_backend.schemas.coinsschema import CoinsCreate, CoinsRead, CoinsUpdate
import uuid
from decimal import Decimal

coins_repo = coinsRepository()

class CoinsService:
    
    def get_coins(self, db: Session, search_type: str, search_value: str):
        if search_type == "id":
            coin = coins_repo.get_coin_by_id(db, id=int(search_value))
        elif search_type == "teacher_id":
            coin = coins_repo.get_coin_by_teacher_id(db, teacher_id=uuid.UUID(search_value))
        elif search_type == "job_id":
            coin = coins_repo.get_coin_by_job_id(db, job_id=uuid.UUID(search_value))
        elif search_type == "payment_id":
            coin = coins_repo.get_coin_by_payment_id(db, payment_id=uuid.UUID(search_value))
        else:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="unavailable search type"
            )
        return coin
    
    def create_coin_record(self, db: Session, data: CoinsCreate):
        return coins_repo.create_coin_record(db, data.model_dump())

    def update_fields(self, db: Session, db_obj, payload: CoinsUpdate):
        if not db_obj:
            raise HTTPException(status_code=404, detail="Coin record not found")

        update_dict = payload.model_dump(exclude_unset=True)

        for restricted_field in ["id", "teacher_id", "job_id", "payment_id", "created_at"]:
            update_dict.pop(restricted_field, None)

        if not update_dict:
            raise HTTPException(status_code=400, detail="No fields provided for update")

        updated_coin = coins_repo.update_coins(db, db_obj, update_dict)
        return updated_coin
        
    def remove_coin_record(self, db: Session, db_obj) -> dict:
        if not db_obj:
            raise HTTPException(status_code=404, detail="Coin record not found")  
        coins_repo.delete_coin_record(db, db_obj)
        return {"message": "Coin record deleted successfully"}
