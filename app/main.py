from fastapi import FastAPI
from pydantic import BaseModel
from .celery import celery_worker

app = FastAPI()

class Calculation(BaseModel):
    delay_amount: int
    x: int
    y: int

@app.post("/")
def index(calculation: Calculation):
    task = celery_worker.create_task.delay(calculation.delay_amount, calculation.x, calculation.y)
    return {"result": task.get()}
