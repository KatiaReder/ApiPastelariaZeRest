from fastapi import APIRouter
from mod_funcionario.Funcionario import Funcionario

router = APIRouter()

@router.get("/funcionario/", tags=["Funcionário"])
def get_funcionario():
    return {"message": "get todos executado" }, 200

@router.get("/funcionario/{id}", tags=["Funcionário"])
def get_funcionario_id(id: int):
    return {"message": f"get do funcionario {id} executado"}, 200

@router.post("/funcionario/", tags=["Funcionário"])
def post_funcionario(f: Funcionario):
    return {"message": "post executado", "nome": f.nome, "cpf": f.cpf, "telefone": f.telefone }, 200

@router.put("/funcionario/{id}", tags=["Funcionário"])
def put_funcionario(id: int, f: Funcionario):
    return {"message": f"put do funcionario {id} executado", "id": id, "nome": f.nome, "cpf": f.cpf, "telefone": f.telefone }, 201

@router.delete("/funcionario/{id}", tags=["Funcionário"])
def delete_funcionario(id: int):
    return {"message": f"delete do funcionario {id} executado"}, 201