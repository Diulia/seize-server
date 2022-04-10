from distutils.log import debug
from fastapi import FastAPI
from sqlalchemy import desc
from sqlalchemy import update
from schemas.registro import Registro
from schemas.crise import Crise
from schemas.fator import Fator
from models.criseModels import Crises as CriseModel
from models.fatorModels import Fatores as FatorModel
from models.registroModels import Registros as RegistroModel
from services.databaseConnector import session


app = FastAPI()

@app.post("/registro")
async def post_registro(id: int, registro: Registro):
    obj_registro = RegistroModel(dia = registro.dia, crise_id = registro.crise_id, fator_id = registro.fator_id)
    session.add(obj_registro)
    session.commit()
    session.refresh(obj_registro)
    return obj_registro

@app.get("/registro")
async def get_registros():
    return session.query(RegistroModel).all()

@app.get("/registro/{id}")
async def get_regId():
   return session.query(RegistroModel).filter(RegistroModel == id)

@app.put("/registro/{id}")
async def put_reg(id: int, registro: Registro):
    session.query(RegistroModel).filter(RegistroModel.id == id).update({'dia': registro.dia, 'crise_id': registro.crise_id, 'fator_id': registro.fator_id })
    session.commit()
    return {"message": "Registro modificado"}

@app.delete("/registro/{id}")
async def delete_registro(id: int):
    session.query(RegistroModel).filter(RegistroModel.id == id).delete()
    session.commit()
    return {"message": "Registro removido"}

# crises
@app.post("/crise")
async def post_crises(crise: Crise):
    obj_crise = CriseModel(descricao = crise.descricao)
    session.add(obj_crise)
    session.commit()
    session.refresh(obj_crise)
    return obj_crise

@app.get("/crise")
async def get_crises():
    return session.query(CriseModel).all()

@app.delete("/crise/{id}")
async def delete_crise(id: int):
    session.query(CriseModel).filter(CriseModel.id == id).delete()
    session.commit()
    return{"message": "Descrição removida"}

@app.put("/crise/{id}")
async def put_crise(id: int, crise: Crise):
    session.query(CriseModel).filter(CriseModel.id == id).update({'descricao': crise.descricao})
    # session.query(CriseModel).filter(CriseModel.id == id).update()
    session.commit()
    return {"message": "Descrição modificada"}

# fatores
@app.post("/fator")
async def post_fator(fator: Fator):
    obj_fator = FatorModel(descricao = fator.descricao)
    session.add(obj_fator)
    session.commit()
    session.refresh(obj_fator)
    return obj_fator

@app.get("/fator")
async def get_fator():
   return session.query(FatorModel).all()

@app.delete("/fator/{id}")
async def delete_fator(id: int):
    session.query(FatorModel).filter(FatorModel.id == id).delete()
    session.commit()
    return{"message": "Descrição removida"}

@app.put("/fator/{id}")
async def put_fator(id: int, fator: Fator):
    session.query(FatorModel).filter(FatorModel.id == id).update({'descricao': fator.descricao})
    session.commit()
    return {"message": "Descrição modificada"}
    
 
 