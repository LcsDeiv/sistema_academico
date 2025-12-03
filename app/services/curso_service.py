from sqlalchemy.orm import Session
from app.models.curso_model import Curso

def criar_curso(db: Session, nome: str, carga_horaria: int):
    novo_curso = Curso(nome=nome, carga_horaria=carga_horaria)
    db.add(novo_curso)
    db.commit()
    db.refresh(novo_curso)
    return novo_curso

def listar_cursos(db: Session):
    return db.query(Curso).all()
