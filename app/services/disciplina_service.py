from sqlalchemy.orm import Session
from app.models.aluno_model import ProfessorModel
from fastapi import HTTPException, status
from datetime import date

class disciplinaService:

    @staticmethod
    def criar_disciplina(db: Session, nome: str, carga_horaria: int, professor_id: int) -> ProfessorModel:
        novo_disciplina = disciplinaModel(
            nome=nome,
            carga_horaria=carga_horaria,
            professor_id=professor_id
        )
        db.add(novo_disciplina)
        db.commit()
        db.refresh(novo_disciplina)
        return novo_disciplina
from app.models.disciplina_model import disciplinaModel