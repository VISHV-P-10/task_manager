from fastapi import FastAPI,status
from app.schemas import TaskCreate, TaskResponse
from fastapi import HTTPException
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

@app.get("/tasks", response_model=list[TaskResponse])
def get_tasks():
    return tasks

@app.get("/tasks/{task_id}",response_model=TaskResponse)
def get_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task
    raise HTTPException(
        status_code=404,
        detail="Task not found"
    )