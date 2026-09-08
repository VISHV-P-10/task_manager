from fastapi import FastAPI,status
#from app.schemas import TaskCreate, TaskResponse, TaskUpdate,TaskPatch
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from app.exceptions import TaskNotFoundException
from app.routers.tasks import router as task_router
app = FastAPI()



@app.exception_handler(TaskNotFoundException)
async def task_not_found_handler(request, exc):
    return JSONResponse(
        status_code=404,
        content={
            "error": "TASK_NOT_FOUND",
            "message": f"Task with id {exc.task_id} was not found"
        }
    )

app.include_router(task_router)


@app.get("/")
def root():
    return {"message": "Task API is running"}