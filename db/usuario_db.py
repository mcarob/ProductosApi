from pydantic import BaseModel
from typing import Dict

class usuarioInDB(BaseModel):
    cod_usuario: int = 0
    correo_usuario: str
    nom_usuario: str
    pass_usuario: str

database_usuario = Dict[int, usuarioInDB]
database_usuario={
            1: usuarioInDB(**{  "cod_usuario":1,
                                "correo_usuario":"Ariana@gmail.com",
                                "nom_usuario":"Ariana",
                                "pass_usuario":"81dc9bdb52d04dc20036dbd8313ed055"
                            }),
            2: usuarioInDB(**{  "cod_usuario":2,
                                "correo_usuario":"Camilo@gmail.com",
                                "nom_usuario":"Camilo Gutierrez",
                                "pass_usuario":"81dc9bdb52d04dc20036dbd8313ed055"
                            }),
            3: usuarioInDB(**{  "cod_usuario":3,
                                "correo_usuario":"carolina@gmail.com",
                                "nom_usuario":"carolina",
                                "pass_usuario":"81dc9bdb52d04dc20036dbd8313ed055"
                            }),
            4: usuarioInDB(**{  "cod_usuario":4,
                                "correo_usuario":"felipe@gmail.com",
                                "nom_usuario":"felipe",
                                "pass_usuario":"81dc9bdb52d04dc20036dbd8313ed055"
                            }),
            5: usuarioInDB(**{  "cod_usuario":5,
                                "correo_usuario":"admin",
                                "nom_usuario":"Administrador",
                                "pass_usuario":"81dc9bdb52d04dc20036dbd8313ed055"
                            }),
                    }
generator = {"id":3}

def save_category(usuario : usuarioInDB):
    # se genera el numero para ingresar a la base de datos (en mysql auto_increment en postgres serial)
    generator["id"]=generator["id"]+1
    usuario.cod_usuario=generator["id"]
    database_usuario[generator["id"]]=usuario
    return usuario

def get_usuario(username : str):
    for i in database_usuario:
        if database_usuario[i].correo_usuario == username:
            return database_usuario[i]
    return None

