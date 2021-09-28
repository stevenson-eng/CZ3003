from fastapi import FastAPI

import models
from api.api import api_router
from db.database import engine

app = FastAPI()
app.include_router(api_router)
models.Base.metadata.create_all(bind=engine)
models.Student.metadata.create_all(bind=engine)


@app.get("/")
def read_root():
    return {"dummy": "return"}
