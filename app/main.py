from fastapi import FastAPI
from app.database import Base, engine
from app.controllers import (
    aluno_controller,
    professor_controller,
    curso_controller,
    disciplina_controller,
    matricula_controller
)

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def root():
    return {"mensagem": "API funcionando com sucesso!"}

app.include_router(aluno_controller.router)
app.include_router(professor_controller.router)
app.include_router(curso_controller.router)
app.include_router(disciplina_controller.router)
app.include_router(matricula_controller.router)
