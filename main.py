from db.category_db import CategoryInDB,get_category,save_category
from db.inventory_db import *
from db.product_db import *
from db.sale_db import *

from models.inventory import *
from models.product import *
from models.category import categoryIn,categoryOut

import datetime
from fastapi import FastAPI
from fastapi import HTTPException

products = FastAPI()

@products.get("/categorias/{peticion}")
async def getCategorias(peticion: str):
    if peticion == "todas":
        return get_category()
    else:
        try:
            peticion=peticion.split(",")
            peticion=[int(numero) for numero in peticion]
            return get_category(peticion)
        except:
             raise HTTPException(status_code=404, detail="Error en la petición de categorias")


@products.put("/categorias/registrarCat/")
async def ingresar_categoria(registro_categoria: CategoryInDB):
    nuevaCategoria=CategoryInDB(**registro_categoria.dict())
    return save_category(nuevaCategoria)