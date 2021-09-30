from fastapi import FastAPI

import models
from api.api import api_router
from db.database import engine

from sqlalchemy.engine import Engine
from sqlalchemy import event


@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()


app = FastAPI()
app.include_router(api_router)
models.Base.metadata.create_all(bind=engine)
models.Student.metadata.create_all(bind=engine)


@app.get("/")
def read_root():
    return {"dummy": "return"}
