from fastapi import FastAPI
from .database import engine
from . import models
from .routers import query_router

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Agent Oriented Programming - Movie Database")

app.include_router(query_router.router)


@app.get("/health")
def health():
    return {"status": "ok"}
