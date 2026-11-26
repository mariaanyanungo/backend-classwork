from fastapi import FastAPI
from database import engine, Base
from pos import models
from pos.routers import product,category, supplier, order
app =FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(product.router)

app.include_router(category.router)
app.include_router(supplier.router)
app.include_router(order.router)