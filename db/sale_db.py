from pydantic import BaseModel
from typing import Dict, List
from datetime import datetime

class SaleInDB(BaseModel):
    cod_sale: int
    number_product: int
    cod_product: List[int]
    cant_product: List[int]
    total_sale: int
    date: datetime

database_sale=[]

generator = {"id":0}

def save_sale(sale_in_db: SaleInDB):
    generator["id"] = generator["id"] + 1
    sale_in_db.cod_sale = generator["id"]
    database_sale.append(sale_in_db)
    return sale_in_db

def getAll_sale():
    return database_sale