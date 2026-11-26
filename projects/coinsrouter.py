from fastapi import APIRouter, Depends, status
from database import get_db
from ttt_backend.schemas.coinsschema import CoinsCreate, CoinsRead, CoinsUpdate
from sqlalchemy.orm import Session
from ttt_backend.services.coinsservices import CoinsService
import uuid

coins_service = CoinsService()

router = APIRouter(prefix="/coins", tags=["coins"])

@router.get("/id/{id}", response_model=list[CoinsRead])
def get_coin_by_id(id: int, db: Session = Depends(get_db)):
    return coins_service.get_coins(db, search_type="id", search_value=str(id))

@router.get("/teacher/{teacher_id}", response_model=list[CoinsRead])
def get_coin_by_teacher_id(teacher_id: uuid.UUID, db: Session = Depends(get_db)):
    return coins_service.get_coins(db, search_type="teacher_id", search_value=str(teacher_id))

@router.get("/job/{job_id}", response_model=list[CoinsRead])
def get_coin_by_job_id(job_id: uuid.UUID, db: Session = Depends(get_db)):
    return coins_service.get_coins(db, search_type="job_id", search_value=str(job_id))

@router.get("/payment/{payment_id}", response_model=list[CoinsRead])
def get_coin_by_payment_id(payment_id: uuid.UUID, db: Session = Depends(get_db)):
    return coins_service.get_coins(db, search_type="payment_id", search_value=str(payment_id))

@router.post("/", response_model=CoinsRead, status_code=status.HTTP_201_CREATED)
def create_coin_record(data: CoinsCreate, db: Session = Depends(get_db)):
    return coins_service.create_coin_record(db, data)

@router.patch("/{id}", response_model=CoinsRead)
def update_coin_fields(id: int, data: CoinsUpdate, db: Session = Depends(get_db)):
    coin_list = coins_service.get_coins(db, search_type="id", search_value=str(id))
    db_obj = coin_list[0] if coin_list else None
    return coins_service.update_fields(db, db_obj, data)

@router.delete("/{id}", status_code=status.HTTP_200_OK)
def delete_coin_record(id: int, db: Session = Depends(get_db)):
    coin_list = coins_service.get_coins(db, search_type="id", search_value=str(id))
    db_obj = coin_list[0] if coin_list else None
    return coins_service.remove_coin_record(db, db_obj)
