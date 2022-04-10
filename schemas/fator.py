from pydantic import BaseModel
from typing import Optional

class Fator(BaseModel):
    id: Optional[int]
    descricao: str