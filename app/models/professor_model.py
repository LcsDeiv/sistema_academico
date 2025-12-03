from sqlalchemy import Column, Integer, String
from app.database import Base

class ProfessorModel(Base):
    __tablename__ = 'professors'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    department = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)