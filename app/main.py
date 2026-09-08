from fastapi import FastAPI,status
from app.schemas import TaskCreate, TaskResponse, TaskUpdate,TaskPatch
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from app.exceptions import TaskNotFoundException
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
        
    raise TaskNotFoundException(task_id)    

@app.put("/tasks/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, task_update: TaskUpdate):

    for task in tasks:
        if task["id"] == task_id:

            task["title"] = task_update.title
            task["description"] = task_update.description
            task["completed"] = task_update.completed

            return task

    raise TaskNotFoundException(task_id)
@app.patch("/tasks/{task_id}", response_model=TaskResponse)
def patch_task(task_id: int, task_patch: TaskPatch):

    for task in tasks:
        if task["id"] == task_id:

            update_data = task_patch.model_dump(exclude_unset=True)

            for field, value in update_data.items():
                task[field] = value

            return task

            raise TaskNotFoundException(task_id)

@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int):

    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            return

    raise TaskNotFoundException(task_id)

@app.exception_handler(TaskNotFoundException)
async def task_not_found_handler(request, exc):
    return JSONResponse(
        status_code=404,
        content={
            "error": "TASK_NOT_FOUND",
            "message": f"Task with id {exc.task_id} was not found"
        }
    )