from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.services import professor_service

router = APIRouter(prefix="/professores", tags=["Professores"])

@router.post("/")
def criar_professor(nome: str, email: str, db: Session = Depends(get_db)):
    try:
        return professor_service.criar_professor(db, nome, email)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/")
def listar_professores(db: Session = Depends(get_db)):
    return professor_service.listar_professores(db)
