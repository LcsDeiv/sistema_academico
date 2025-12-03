from sqlalchemy.orm import Session
from app.models.professor_model import Professor

def criar_professor(db: Session, nome: str, email: str):
    professor_existente = db.query(Professor).filter(Professor.email == email).first()
    if professor_existente:
        raise ValueError("Email já cadastrado!")

    novo_professor = Professor(nome=nome, email=email)
    db.add(novo_professor)
    db.commit()
    db.refresh(novo_professor)
    return novo_professor


def listar_professores(db: Session):
    return db.query(Professor).all()
