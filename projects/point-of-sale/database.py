from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
from dotenv import load_dotenv

load_dotenv()

DATA_BASE_URL=os.environ.get("DATA_BASE_URL")

engine=create_engine(DATA_BASE_URL, echo=True, future=True)
Session=sessionmaker(bind=engine)


Base=declarative_base()

def get_db():
    db=Session()
    try:
        yield db
    finally:
        db.close()
        