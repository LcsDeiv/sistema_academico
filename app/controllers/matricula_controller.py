from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.services import matricula_service

router = APIRouter(prefix="/matriculas", tags=["Matrículas"])

@router.post("/")
def criar_matricula(
    aluno_id: int,
    curso_id: int,
    db: Session = Depends(get_db)
):
    return matricula_service.criar_matricula(db, aluno_id, curso_id)

@router.get("/")
def listar_matriculas(db: Session = Depends(get_db)):
    return matricula_service.listar_matriculas(db)
