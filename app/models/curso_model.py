from sqlalchemy import Column, Integer, String
from app.database import Base

class cursoModel(Base):
    __tablename__ = 'cursos'

    id= Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    duracao = Column(Integer, nullable=False)