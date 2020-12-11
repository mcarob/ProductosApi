from pydantic import BaseModel

class categoryIn(BaseModel):
    cod_category: int
    nom_category: str

class categoryOut(BaseModel):
    cod_category: int
    nom_category: str

