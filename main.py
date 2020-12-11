from db.category_db import CategoryInDB,getAll_category,save_category
from models.category import categoryIn,categoryOut
import datetime
from fastapi import FastAPI
from fastapi import HTTPException

products = FastAPI()

@products.get("/categorias/{peticion}")
async def getCategorias(peticion: str):
    if peticion == "todas":
        return getAll_category()
    else:
        try:
            buscar=int(peticion)

        except expression as identifier:
             raise HTTPException(status_code=404, detail="Error en la petición de categorias")


@products.put("/categorias/registrarCat/")
async def ingresar_categoria(registro_categoria: CategoryInDB):
    nuevaCategoria=CategoryInDB(**registro_categoria.dict())
    return save_category(nuevaCategoria)