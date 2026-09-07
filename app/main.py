from fastapi import FastAPI,status
from app.schemas import TaskCreate
app = FastAPI()

tasks = []
@app.get("/")
def home():
    return {"message": "Task Management API is running"}

@app.post("/tasks",status_code=status.HTTP_201_CREATED)
def create_task(task: TaskCreate):

    new_task = {
        "id": len(tasks) + 1,
        "title": task.title,
        "description": task.description,
        "completed": task.completed
    }

    tasks.append(new_task)

    return new_task