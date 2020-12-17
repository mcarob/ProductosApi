from pydantic import BaseModel
from typing import Dict

class CategoryInDB(BaseModel):
    cod_category: int = 0
    nom_category: str ="galletas"

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

def get_category(cod=[]):
    if len(cod)==0:
        return database_category
    else:
        dic_filtrado={}
        for key in database_category.keys():
            print( database_category[key]["cod_category"])
            if database_category[key]["cod_category"]==cod:
                dic_filtrado[key]=database_category[key]
        return dic_filtrado

