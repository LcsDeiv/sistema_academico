from sqlalchemy import Column, Integer, String
from app.database import Base

class cursoModel(Base):
    __tablename__ = 'cursos'

    id= Column(Integer, primary_key=True, index=True)
    nome_curso = Column(String, nullable=False)
    carga_horaria = Column(Integer, nullable=False)