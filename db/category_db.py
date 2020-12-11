from pydantic import BaseModel
from typing import Dict

class CategoryInDB(BaseModel):
    cod_category: int 
    nom_category: str = "General"

database_category = Dict[int, CategoryInDB]
database_category={
            1: CategoryInDB(**{  "cod_category":1,
                                "nom_category":"Frutas Secas"
                            }),
            2: CategoryInDB(**{  "cod_category":2,
                                "nom_category":"Frutas"
                            }),
            3: CategoryInDB(**{  "cod_category":3,
                                "nom_category":"Enlatados"
                            }),
                    }
generator = {"id":3}

def save_category(CategoryIn : CategoryInDB):
    # se genera el numero para ingresar a la base de datos (en mysql auto_increment en postgres serial)
    generator["id"]=generator["id"]+1
    CategoryIn.cod_category=generator["id"]
    database_category[generator["id"]]=CategoryIn
    return CategoryIn

def getAll_category():
    return database_category