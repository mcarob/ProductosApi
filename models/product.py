from pydantic import BaseModel


class productIn(BaseModel):
    cod_product: int
    nom_product: int
    cod_category: int


class productOut(BaseModel):
    cod_product: int
    nom_product: int
    nom_category: str


