from pydantic import BaseModel
from typing import Optional


class Crise(BaseModel):
    id: Optional[int]
    descricao: str