from sqlalchemy.orm import Session
from app.models.matricula_model import Matricula

def criar_matricula(db: Session, aluno_id: int, curso_id: int):
    nova_matricula = Matricula(
        aluno_id=aluno_id,
        curso_id=curso_id
    )

    db.add(nova_matricula)
    db.commit()
    db.refresh(nova_matricula)
    return nova_matricula


def listar_matriculas(db: Session):
    return db.query(Matricula).all()
