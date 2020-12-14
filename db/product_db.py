from pydantic import BaseModel
from typing import Dict

class ProductInDB(BaseModel):
    cod_product: int
    nom_product: str
    cod_category: str
    purchase_price: int
    sale_price: int
    dist_product: str

database_product = Dict[int, ProductInDB]
database_product={
            1: ProductInDB(**{  "cod_product":1,
                                "nom_product":"Arándanos",
                                "cod_category":1,
                                "purchase_price":2500,
                                "sale_price":4500,
                                "dist_product":"Frecampo"

                            }),
            2: ProductInDB(**{  "cod_product":2,
                                "nom_product":"Atún",
                                "cod_category":3,
                                "purchase_price":1000,
                                "sale_price":2000,
                                "dist_product":"Ekono"
                            }),
            3: ProductInDB(**{  "cod_product":1,
                                "nom_product":"Manzana",
                                "cod_category":2,
                                "purchase_price":600,
                                "sale_price":1000,
                                "dist_product":"Frecampo"
                            })
                    }

generator = {"id":3}

def save_product(product_in_db: ProductInDB):
    generator["id"] = generator["id"] + 1
    product_in_db.cod_product = generator["id"]
    database_product.append(product_in_db)
    return product_in_db

def getAll_product():
    return database_product
