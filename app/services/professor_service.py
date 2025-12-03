from sqlalchemy.orm import Session
from app.models.aluno_model import ProfessorModel
from fastapi import HTTPException, status
from datetime import date

class ProfessorService:

    @staticmethod
    def criar_professor(db: Session, nome: str, departamento: str, email: str) -> ProfessorModel:
        existing_professor = db.query(ProfessorModel).filter(ProfessorModel.email == email).first()
        if existing_professor:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email Já Cadastrado."
            )
        novo_professor = ProfessorModel(nome=nome, departamento=departamento, email=email)
        db.add(novo_professor)
        db.commit()
        db.refresh(novo_professor)
        return novo_professor
    
    
