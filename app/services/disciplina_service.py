from sqlalchemy.orm import Session
from app.models.disciplina_model import Disciplina

def criar_disciplina(db: Session, nome: str, carga_horaria: int, curso_id: int):
    nova_disciplina = Disciplina(
        nome=nome,
        carga_horaria=carga_horaria,
        curso_id=curso_id
    )

    db.add(nova_disciplina)
    db.commit()
    db.refresh(nova_disciplina)
    return nova_disciplina


def listar_disciplinas(db: Session):
    return db.query(Disciplina).all()
