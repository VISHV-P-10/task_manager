from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Task Management API is running"}