from sqlalchemy.orm import Session
from app.models.aluno_model import ProfessorModel
from fastapi import HTTPException, status
from datetime import date

class cursoService:

    @staticmethod
    def criar_curso(db: Session, nome: str, duracao: int) -> cursoModel:
        novo_curso = cursoModel(
            nome=nome,
            duracao=duracao
        )
        db.add(novo_curso) 
        db.commit()
        db.refresh(novo_curso)
        return novo_curso
from app.models.curso_model import cursoModel 