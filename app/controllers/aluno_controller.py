from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.services import aluno_service
from datetime import date

router = APIRouter(prefix="/alunos",  tags=["Alunos"])

@router.post("/")
def criar_aluno(nome: str, email: str, data_nascimento: date, db: Session = Depends(get_db)):
    try:
        return aluno_service.criar_aluno(db,nome,email,data_nascimento)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.get("/")

def listar_alunos(db:Session = Depends(get_db)):
    return aluno_service.listar_alunos(db)