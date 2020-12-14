from pydantic import BaseModel
from typing import Dict
from datetime import datetime

class InventoryInDB(BaseModel):
    cod_inventory: int
    cod_product: int
    nom_product: str
    cant_product: int #Entrada o salida del producto
    total_product: int # Balance
    date: datetime

database_inventory = []

generator = {"id":0}

def save_inventory(InventoryIn : InventoryInDB):
    generator["id"]=generator["id"]+1
    InventoryIn.cod_inventory=generator["id"]
    database_inventory[generator["id"]]=InventoryIn
    return InventoryIn

def getAll_Inventory():
    return database_inventory
