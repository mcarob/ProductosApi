from pydantic import BaseModel

class saleIn(BaseModel):
    number_product: int
    cod_product: List[int]
    cant_product: List[int]

class saleOut(BaseModel):
    cod_sale: int
    number_product: int
    cod_product: List[int]
    cant_product: List[int]
    total_sale: int
    date: datetime