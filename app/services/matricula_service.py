from sqlalchemy.orm import Session
from app.models.aluno_model import MatriculaModel
from fastapi import HTTPException, status
from datetime import date

class MatriculaService:
    @staticmethod
    def criar_matricula(db: Session, nome_estudante: str, curso: str, enrollment_date: str) -> MatriculaModel:
        novo_matricula = MatriculaModel(
            student_name=nome_estudante,
            course=curso,
            enrollment_date=enrollment_date
        )
        db.add(novo_matricula)
        db.commit()
        db.refresh(novo_matricula)
        return novo_matricula
from app.models.matricula_model import MatriculaModel