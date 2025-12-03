from sqlalchemy import Column, Integer, Strin
from app.database import Base

class MatriculaModel(Base):
    __tablename__ = 'matriculas'

    id = Column(Integer, primary_key=True, index=True)
    student_name = Column(String, nullable=False)
    course = Column(String, nullable=False)
    enrollment_date = Column(String, nullable=False)