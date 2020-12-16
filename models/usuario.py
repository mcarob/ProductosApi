from pydantic import BaseModel

class usuarioIn(BaseModel):
    correo_usuario: str
    pass_usuario: str

class usuarioOut(BaseModel):
    cod_usuario: int
    correo_usuario: str
    nom_usuario: str

