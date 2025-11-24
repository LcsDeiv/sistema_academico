from fatapi import FastAPI
from app.database import Base, engine
from app.controllers import aluno_controller

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(aluno_controller.router)
