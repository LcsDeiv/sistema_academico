from sqlalchemy import Column, Integer, String
from app.database import Base

class disciplinaModel(Base):
    __tablename__ = 'disciplinas'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    carga_horaria = Column(Integer, nullable=False)
    professor_id = Column(Integer, nullable=False)