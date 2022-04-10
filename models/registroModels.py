from sqlalchemy import Column, ForeignKey, Integer, Date
from sqlalchemy.orm import relationship
from services.databaseConnector import Base



class Registros(Base):
    __tablename__ = "registros"

    id = Column(Integer, primary_key=True, index=True)
    dia = Column(Date, index=True)
    crise_id = Column(Integer, ForeignKey("crises.id"), index=True)
    fator_id = Column(Integer, ForeignKey("fatores.id"), index=True)

