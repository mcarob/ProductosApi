from pydantic import BaseModel
from typing import Dict


    # cod_producto: int
    # nom_producto: str
    # cod_category: int
    # detalle_producto: str
    # cantidad_producto: int
    # precio_compra: int
    # precio_venta: int
class ProductInDB(BaseModel):
    cod_producto: int =0
    nom_producto: str
    cod_category: int
    precio_compra: int
    precio_venta: int
    detalle_producto: str
    cantidad_producto: int =0


database_product = Dict[int, ProductInDB]
database_product={
            1: ProductInDB(**{  "cod_producto":1,
                                "nom_producto":"Arándanos",
                                "cod_category":1,
                                "precio_compra":2500,
                                "precio_venta":4500,
                                "detalle_producto":"fruta roja x500gr",
                                "cantidad_producto":0

                            }),
            2: ProductInDB(**{  "cod_producto":2,
                                "nom_producto":"Atún",
                                "cod_category":3,
                                "precio_compra":2500,
                                "precio_venta":4500,
                                "detalle_producto":"atún sin mercurio x300gr",
                                "cantidad_producto":0
                            }),
            3: ProductInDB(**{  "cod_producto":3,
                                "nom_producto":"Manzana",
                                "cod_category":2,
                                "precio_compra":3000,
                                "precio_venta":5000,
                                "detalle_producto":"Manzana organica 1kg",
                                "cantidad_producto":0
                            })
                    }

generator = {"id":3}

def save_product(product_in_db: ProductInDB):
    print(generator["id"])
    generator["id"] = generator["id"] + 1
    product_in_db.cod_producto = generator["id"]
    database_product[generator["id"]]=product_in_db
    return product_in_db

def getAll_product():
    return database_product
