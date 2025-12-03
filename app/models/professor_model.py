from sqlalchemy import Column, Integer, String
from app.database import Base

class Professor(Base):
    _tablename_ = "professores"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)