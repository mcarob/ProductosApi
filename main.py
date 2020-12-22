from db.inventory_db import *
from db.product_db import *
from db.sale_db import *
from db.usuario_db import *
from models.usuario import *
from models.inventory import *
from models.product import *
from db.category_db import CategoryInDB,get_category,save_category
from models.category import categoryIn,categoryOut
import datetime
import hashlib 
from fastapi import FastAPI
from fastapi import HTTPException
from fastapi.middleware.cors import CORSMiddleware

products = FastAPI()

origins = [
    "http://localhost:8080",
]
products.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@products.get("/categorias/{peticion}")
def getCategorias(peticion: str):
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
def ingresar_categoria(registro_categoria: CategoryInDB):
    nuevaCategoria=CategoryInDB(**registro_categoria.dict())
    return save_category(nuevaCategoria)


@products.post("/usuarios/auth/")
async def buscarUsuario(usuarioC : usuarioIn):
    respuestadb=get_usuario(usuarioC.correo_usuario)
    if respuestadb!= None :
        if(respuestadb.pass_usuario==usuarioC.pass_usuario):
            return usuarioOut(**respuestadb.dict())
        else:
            raise HTTPException(status_code=201, detail="La contraseña es incorrecta")
    else:
        raise HTTPException(status_code=201, detail="El correo no existe en la base de datos")

@products.get("/productos/{peticion}")
def getProductos(peticion: str):
    database_productout = Dict[int, productOut]
    database_productout={}
    if peticion == "todas":
        productosTodos=getAll_product()
        for producto in productosTodos:
            cod_categoria=productosTodos[producto].cod_category
            producto1=get_category([cod_categoria])[cod_categoria]
            print(producto1['nom_category'])

            database_productout[producto]=productOut(**productosTodos[producto].dict(),nom_category = producto1['nom_category'])
        return database_productout
    raise HTTPException(status_code=404, detail="Error en la petición de categorias")


@products.put("/categorias/registrarProduct/")
def ingresar_productos(productoIn: ProductInDB):
    nuevoProducto=ProductInDB(**productoIn.dict())
    return save_product(nuevoProducto)
