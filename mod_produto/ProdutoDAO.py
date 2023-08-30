from fastapi import APIRouter
from mod_produto.Produto import Produto

router = APIRouter()

@router.get("/produto/", tags=["Produto"])
def get_produto():
    return {"message": "get todos executado" }, 200

@router.get("/produto/{id}", tags=["Produto"])
def get_produto_id(id: int):
    return {"message": "get do produto executado"}, 200

@router.post("/produto/", tags=["Produto"])
def post_produto(p: Produto):
    return {"message": "post executado", "nome": p.nome, "descricao": p.descricao}, 200

@router.put("/produto/{id}", tags=["Produto"])
def put_produto(id: int, p: Produto):
    return {"message": "put do produto executado", "id": id, "nome": p.nome, "descricao": p.descricao }, 201

@router.delete("/produto/{id}", tags=["Produto"])
def delete_produto(id: int):
    return {"message": "delete do produto executado"}, 201