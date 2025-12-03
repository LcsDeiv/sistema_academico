from sqlalchemy import Column, Integer, String
from app.database import Base

class MatriculaModel(Base):
    __tablename__ = 'matriculas'

    id = Column(Integer, primary_key=True, index=True)
    nome_estudante = Column(String, nullable=False)
    curso = Column(String, nullable=False)
    data_inscricao = Column(String, nullable=False)