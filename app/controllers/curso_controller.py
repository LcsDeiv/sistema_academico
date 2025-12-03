from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.services import curso_service

router = APIRouter(prefix="/cursos", tags=["Cursos"])

@router.post("/")
def criar_curso(nome: str, carga_horaria: int, db: Session = Depends(get_db)):
    return curso_service.criar_curso(db, nome, carga_horaria)

@router.get("/")
def listar_cursos(db: Session = Depends(get_db)):
    return curso_service.listar_cursos(db)