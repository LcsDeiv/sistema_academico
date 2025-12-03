from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.services import disciplina_service

router = APIRouter(prefix="/disciplinas", tags=["Disciplinas"])

@router.post("/")
def criar_disciplina(
    nome: str,
    carga_horaria: int,
    curso_id: int,
    db: Session = Depends(get_db)
):
    return disciplina_service.criar_disciplina(db, nome, carga_horaria, curso_id)

@router.get("/")
def listar_disciplinas(db: Session = Depends(get_db)):
    return disciplina_service.listar_disciplinas(db)