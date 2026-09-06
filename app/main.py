from fastapi import FastAPI
from app.schemas import TaskCreate
app = FastAPI()


@app.get("/")
def home():
    return {"message": "Task Management API is running"}

@app.post("/tasks")
def create_task(task: TaskCreate):
    return task