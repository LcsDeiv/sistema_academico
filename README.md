# *_Sistema Acadêmico– API em FastAPI_*
---
Este projeto é uma API REST construída com FastAPI, SQLAlchemy e SQLite, seguindo o padrão de arquitetura em 3 camadas (Controller, Service e Model).
O objetivo é fornecer uma base sólida para um sistema acadêmico simples, permitindo gerenciar entidades como Aluno, Curso e Disciplina.

## 🔥 Tecnologias que seram utilizadas

Python 3.10+

FastAPI

Uvicorn

SQLAlchemy ORM

Pydantic

SQLite 

## 🧱  Arquitetura utilizada

A aplicação segue o padrão 3 camadas, separando responsabilidades:

Controllers → Endpoints da API

Services → Regras de negócio

Models → Mapeamento das tabelas (SQLAlchemy)

Essa abordagem deixa o sistema organizado, escalável e fácil de entender.

---
# Como instalar as dependências (requirements.txt)

### Antes de tudo, garanta que você tem o Python 3.10+ instalado.

### Crie e ative um ambiente virtual (opcional, porém recomendado):

``` python -m venv venv ```


Ativar no Windows:

``` venv\Scripts\activate ```


Ativar no Linux/Mac:

``` source venv/bin/activate ```


Instale todas as dependências:

``` pip install -r requirements.txt ```

🚀 Como rodar o projeto

Após instalar as dependências, execute o comando:

```uvicorn main:app --reload```


