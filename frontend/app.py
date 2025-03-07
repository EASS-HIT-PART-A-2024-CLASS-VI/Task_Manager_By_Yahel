import streamlit as st
import requests

# כותרת הממשק
st.title("Task Manager")

# **הוספת משימה חדשה**
st.header("Create a New Task")

# קלט עבור פרטי המשימה
title = st.text_input("Task Title")
description = st.text_area("Task Description")
category = st.text_input("Category")
due_date = st.text_input("Due Date (YYYY-MM-DD)")  # ודא שהתאריך בפורמט הנכון
priority = st.selectbox("Priority", ["High", "Medium", "Low"])
status = st.selectbox("Status", ["Pending", "In Progress", "Completed"])

# כפתור לשליחת בקשה ליצירת משימה
if st.button("Create Task"):
    # יצירת מילון עם פרטי המשימה
    task_data = {
        "title": title,
        "description": description,
        "category": category,
        "due_date": due_date,  # ודא שהתאריך בפורמט הנכון
        "priority": priority,
        "status": status
    }

    # שליחת בקשה ל-Backend (API של FastAPI)
    response = requests.post("http://backend:8000/tasks", json=task_data)

    if response.status_code == 200:
        task = response.json()
        st.success(f"Task Created: {task['title']}")
        st.write(f"Task ID: {task['id']}")  # הצגת ה-ID שהתקבל
    else:
        st.error(f"Failed to create task. Status code: {response.status_code}")
        st.write(response.json())  # הצגת הודעת השגיאה שהתקבלה

# **שליפת משימה לפי ID**
st.header("Get Task by ID")

# תיבת קלט לקבלת ID של משימה
task_id = st.text_input("Enter task ID:")

# כפתור לשלוח בקשה ל-Backend
if st.button("Get Task"):
    # שליחת בקשה ל-Backend (API של FastAPI)
    url = f"http://backend:8000/tasks/{task_id}"
    response = requests.get(url)

    if response.status_code == 200:
        # הצגת המידע שהתקבל מה-API
        task = response.json()

        # הצגת כל המידע שמתקבל מה-API
        if 'id' in task:
            st.write(f"Task ID: {task['id']}")
            st.write(f"Task Title: {task['title']}")
            st.write(f"Task Description: {task['description']}")
            st.write(f"Task Category: {task['category']}")
            st.write(f"Task Due Date: {task['due_date']}")
            st.write(f"Task Priority: {task['priority']}")
            st.write(f"Task Status: {task['status']}")
        else:
            st.error("Task ID not found.")
    else:
        st.error(f"Failed to fetch task with ID {task_id}. Task might not exist.")
