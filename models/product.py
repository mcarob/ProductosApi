from pydantic import BaseModel


class productIn(BaseModel):
    cod_producto: int
    nom_producto: str
    cod_category: int
    detalle_producto: str
    cantidad_producto: int
    precio_compra: int
    precio_venta: int


class productOut(BaseModel):
    cod_product: int
    nom_product: str
    nom_category: str
    detalle_producto: str
    cantidad_producto: int
    precio_compra: int
    precio_venta: int


