from pydantic import BaseModel

class Produto(BaseModel):
  id_produto: int = None
  nome: str
  descricao: str
  foto: dict = None
  valor_unitario: float