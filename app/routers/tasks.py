from fastapi import APIRouter, status
from app.schemas import TaskCreate, TaskResponse, TaskUpdate, TaskPatch
from app.exceptions import TaskNotFoundException
#from app.services.task_service import create_task
from app.services.task_service import (
    create_task,
    get_tasks,
    get_task,
    update_task,
    patch_task,
    delete_task,
)
router = APIRouter()
tasks = []
@router.post("/tasks", status_code=status.HTTP_201_CREATED)
def create_task_endpoint(task: TaskCreate):
    return create_task(task)

@router.get("/tasks", response_model=list[TaskResponse])
def get_tasks_endpoint():
    return get_tasks()

@router.get("/tasks/{task_id}", response_model=TaskResponse)
def get_task_endpoint(task_id: int):
    return get_task(task_id)

@router.put("/tasks/{task_id}", response_model=TaskResponse)
def update_task_endpoint(task_id: int, task_update: TaskUpdate):
    return update_task(task_id, task_update)

@router.patch("/tasks/{task_id}", response_model=TaskResponse)
def patch_task_endpoint(task_id: int, task_patch: TaskPatch):
    return patch_task(task_id,task_patch)

@router.delete(
    "/tasks/{task_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_task_endpoint(task_id: int):
    delete_task(task_id)