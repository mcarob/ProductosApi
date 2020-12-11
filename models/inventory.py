from pydantic import BaseModel
from datetime import datetime

class inventoryIn(BaseModel):
    cod_inventory: int
    cod_producto: int
    total_product: int

class inventoryOut(BaseModel):
    cod_inventory: int
    nom_product: str
    total_product: int
    date: datetime 

