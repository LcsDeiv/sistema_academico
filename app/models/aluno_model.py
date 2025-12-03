from sqlalchemy import Column, Integer, String, Date
from app.database import Base 

class Aluno (Base):
    __tablename__ = "alunos"

    id= Column(Integer, primary_key=True, index=True)
    nome_aluno = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    data_nascimento = Column(Date, nullable=False)