from pydantic import BaseModel
from typing import  Optional

class Registro(BaseModel):
    id: Optional[int]
    dia: str
    crise_id: int
    fator_id: int
    
