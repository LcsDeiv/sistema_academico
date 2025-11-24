from sqlalchemy.orm import Session
from app.models.aluno_model import Aluno
from fastapi import HTTPException, status
from datetime import date

def criar_aluno(db: Session, nome: str, email:str, data_nascimento: date):
    aluno_existente = db.query(Aluno).filter (Aluno.email==email).first()
    if aluno_existente:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, 
            detail="Email já cadastrado!"
        )
    
    novo_aluno = Aluno (nome=nome, email=email, data_nascimento=data_nascimento)
    db.add(novo_aluno)
    db.commit()
    db.refresh(novo_aluno)
    return novo_aluno

def listar_alunos(db:Session):
    return db.query(Aluno).all()