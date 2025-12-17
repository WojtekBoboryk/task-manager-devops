from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Task Manager API")

TASKS = []
NEXT_ID = 1

class TaskIn(BaseModel):
    title: str

@app.get("/api/health")
def health():
    return {"status": "ok"}

@app.get("/api/tasks")
def list_tasks():
    return TASKS

@app.post("/api/tasks")
def create_task(task: TaskIn):
    global NEXT_ID
    item = {"id": NEXT_ID, "title": task.title}
    NEXT_ID += 1
    TASKS.append(item)
    return item

@app.delete("/api/tasks/{task_id}")
def delete_task(task_id: int):
    global TASKS
    TASKS = [t for t in TASKS if t["id"] != task_id]
    return {"deleted": task_id}
