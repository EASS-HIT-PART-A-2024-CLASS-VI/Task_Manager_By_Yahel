# Task_Manager_By_Yahel

**Task Manager** is a full-stack application designed to help users efficiently manage their tasks. Built using **FastAPI** for the backend and **Streamlit** for the frontend, it provides a simple interface for task management. The application is containerized using **Docker** and orchestrated with **Docker Compose**, ensuring smooth integration between the frontend, backend, and PostgreSQL database.

🎥 **Watch a demo of the Task Manager in action:** [YouTube Link](#)

---

## 🔧 System Design Overview

This section provides an overview of the major components in the Task Manager system and their respective roles.

---

## 📊 Project Diagram

- **Frontend (Streamlit):** Provides the user interface to interact with tasks and task details.
- **Backend (FastAPI):** Handles core logic such as CRUD operations for task management.
- **Database (PostgreSQL):** Stores task-related data persistently.
- **Docker Compose:** Orchestrates the services to ensure smooth communication between the frontend, backend, and database.

---

## ⚙️ Components

- **Frontend:** Simple and intuitive interface, built with Streamlit, allowing users to create, view, update, and delete tasks.
- **Backend API:** Exposed via FastAPI, it manages task operations (CRUD).
- **Database:** PostgreSQL is used to store task-related data.

---

## 🗂️ Project Structure

The repository is organized as follows:

├── backend/                     # Contains FastAPI backend code for task management logic
│   ├── main.py                  # API routes and logic for task management
│   └── models.py                # Database models and schemas
├── frontend/                    # Contains the Streamlit frontend application
│   └── streamlit_app.py         # Main application file
├── docker-compose.yml           # Docker Compose configuration for orchestrating services
├── requirements.txt             # Dependencies for both frontend and backend
├── README.md                    # Project documentation
└── .gitignore                   # Files to be ignored by git


---

## 🖥️ API Endpoints Overview

### - **Create a new task:**

**Request Body:**
{
  "title": "Task Title",
  "description": "Task Description",
  "category": "Task Category",
  "due_date": "YYYY-MM-DD",
  "priority": "High",
  "status": "Pending"
}

**Response Body:**
{
  "id": "uuid-generated-id",
  "title": "Task Title",
  "description": "Task Description",
  "category": "Task Category",
  "due_date": "YYYY-MM-DD",
  "priority": "High",
  "status": "Pending"
}

Retrieve a task by its ID:

**Response Body:**
{
  "id": "task-id",
  "title": "Task Title",
  "description": "Task Description",
  "category": "Task Category",
  "due_date": "YYYY-MM-DD",
  "priority": "High",
  "status": "Pending"
}


- Update an existing task:

**Request Body:**
{
  "title": "Updated Task Title",
  "description": "Updated Task Description",
  "category": "Updated Category",
  "due_date": "Updated Due Date",
  "priority": "Medium",
  "status": "In Progress"
}

**Response Body:**
{
  "id": "task-id",
  "title": "Updated Task Title",
  "description": "Updated Task Description",
  "category": "Updated Category",
  "due_date": "Updated Due Date",
  "priority": "Medium",
  "status": "In Progress"
}



- Delete a task by its ID:

**Response Body:**
{
  "message": "Task task-id deleted"
}



🚀 How to Run the Project
**System Requirements**
Ensure the following dependencies are installed before setting up the project:

Docker: Download Docker
Docker Compose: Install Docker Compose
Python 3.8+: Make sure you have Python version 3.8 or higher installed.

**Installation Steps**

Clone the Repository:
git clone https://github.com/your-username/task-manager.git
cd task-manager

Build and Run the Project Using Docker Compose:
docker-compose up --build

This will:
1.Build the backend and frontend services.
2. Start the PostgreSQL database.
3. Expose the necessary ports:
Frontend UI: http://localhost:8501
Backend API: http://localhost:8000

**Access the System:**

Frontend (UI): Open http://localhost:8501 in your browser to interact with the UI.
Backend (API): Access the backend API at http://localhost:8000.

**Stopping the System:**
To stop the system, run the following command:
docker-compose down


🤝 Contributing

We welcome contributions! If you'd like to contribute, follow these steps:

1. Fork the repository and clone it to your machine:

git clone https://github.com/your-username/task-manager.git
cd task-manager

2. Create a new branch:

git checkout -b feature-branch

3. Make your changes, then commit and push them to your branch:

git commit -am 'Add a new feature or fix a bug'
git push origin feature-branch

4. Open a pull request to merge your changes into the main branch.


## 🙏 Thank You for Using the Project!

Thank you for using Task Manager!
I hope the project helped you manage your tasks efficiently and effectively.
