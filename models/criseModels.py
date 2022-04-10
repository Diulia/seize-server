from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from services.databaseConnector import Base

class Crises(Base):
    __tablename__ = "crises"

    id = Column(Integer, primary_key=True, index=True)
    descricao = Column(String, index=True)