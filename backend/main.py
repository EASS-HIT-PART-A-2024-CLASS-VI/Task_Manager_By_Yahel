from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, validator
from typing import List
from uuid import uuid4
from datetime import datetime

app = FastAPI()

# מודל של משימה
class Task(BaseModel):
    id: str = None  # השדה הזה לא חייב להיות בהתחלה
    title: str
    description: str
    category: str
    due_date: str  # תאריך חייב להיות בפורמט 'YYYY-MM-DD'
    priority: str
    status: str

    # ווידוא שהתאריך בפורמט הנכון
    @validator('due_date')
    def validate_due_date(cls, value):
        try:
            # אם התאריך לא נכון, תתפוס את השגיאה ותחזיר הודעה
            datetime.strptime(value, '%Y-%m-%d')
        except ValueError:
            raise ValueError('Invalid date format. Use YYYY-MM-DD.')
        return value

# רשימה לשמירת המשימות (במקום בסיס נתונים)
tasks = []

@app.post("/tasks", response_model=Task)
def create_task(task: Task):
    task_id = str(uuid4())  # יצירת ID חדש
    task_dict = task.dict()  # המרת המודל של המשימה לדיקשנרי
    task_dict["id"] = task_id  # הוספת ה-ID למילון
    tasks.append(task_dict)  # הוספת המשימה לרשימה
    return Task(**task_dict)  # החזרת אובייקט מסוג Task עם כל השדות

@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: str):
    for t in tasks:
        if t["id"] == task_id:
            return t
    raise HTTPException(status_code=404, detail="Task not found")

# שאר הפעולות כמו עדכון, מחיקה, ושליפת כל המשימות נשארות ללא שינוי
@app.get("/tasks", response_model=List[Task])
def get_tasks():
    return tasks

@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: str, task: Task):
    for t in tasks:
        if t["id"] == task_id:
            updated_task = t.copy()
            if task.title:
                updated_task["title"] = task.title
            if task.description:
                updated_task["description"] = task.description
            if task.category:
                updated_task["category"] = task.category
            if task.due_date:
                updated_task["due_date"] = task.due_date
            if task.priority:
                updated_task["priority"] = task.priority
            if task.status:
                updated_task["status"] = task.status
            t.update(updated_task)
            return t
    return {"error": "Task not found"}

@app.delete("/tasks/{task_id}")
def delete_task(task_id: str):
    global tasks
    tasks = [t for t in tasks if t["id"] != task_id]
    return {"message": f"Task {task_id} deleted"}
