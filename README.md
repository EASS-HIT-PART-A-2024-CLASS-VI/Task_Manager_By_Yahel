# YahelN_Task_maneger_project
# Task-manager-project

**Task Manager** is a full-stack application built to help users manage their tasks effectively. 
The backend is powered by **FastAPI** and handles the API logic, including CRUD operations (Create, Read, Update, Delete). The frontend is built using **Streamlit**, providing a simple interface to create, view, update, and delete tasks. The application is containerized using **Docker** and orchestrated with **Docker Compose**, ensuring smooth integration between the frontend, backend, and the PostgreSQL database.

## Features
- **Task Creation**: Users can create new tasks with details like title, description, category, due date, priority, and status.
- **Task Retrieval**: Users can retrieve tasks by their ID to view details.
- **Task Update**: Users can update existing tasks, including task details like priority, status, and description.
- **Task Deletion**: Users can delete tasks from the list.
- **User-Friendly Interface**: The frontend interface is simple and intuitive, built using Streamlit.

## System Requirements
Ensure the following are installed before setting up the project:

- **Docker** – Download and install Docker from [here](https://www.docker.com/get-started).
- **Docker Compose** – Install Docker Compose from [here](https://docs.docker.com/compose/install/).
- **Python 3.8+** – Ensure you have Python version 3.8 or higher.

## Installation and Setup Instructions

### 1. Install Docker
To install Docker, follow the instructions for your operating system:
- **Windows/macOS**: Download Docker Desktop [here](https://www.docker.com/products/docker-desktop).
- **Linux**: Follow the installation instructions [here](https://docs.docker.com/engine/install/).

### 2. Clone the Repository
Clone the repository and navigate into the project directory:

git clone https://github.com/your-username/task-manager.git
cd task-manager
3. Build and Run the Project Using Docker Compose

To start the application, use Docker Compose to build and run the containers --> docker-compose up --build

This will:

- Build the backend and frontend services.
- Start the PostgreSQL database.
- Expose the necessary ports:
- Frontend UI will be available at http://localhost:8501.
- Backend API will be available at http://localhost:8000.

4. Access the System
Once the containers are running, you can interact with the application:

Frontend (UI): Open http://localhost:8501 in your browser to start interacting with the UI.
Backend (API): Access the backend API for task management at http://localhost:8000.

5. Stopping the System
To stop the system, use the following command:

docker-compose down


**Folder Structure
The repository is organized as follows:

backend/:  Contains the FastAPI backend code that handles the task management logic (routes for creating, updating, deleting tasks).
frontend/:  Contains the Streamlit frontend application where users interact with the system.
docker/:  Contains Docker-related files for both frontend and backend services.
docker-compose.yml: The Docker Compose file which connects the frontend, backend, and database.
requirements.txt: List of dependencies for both frontend and backend services.


API Endpoints
POST /tasks

Create a new task.

Request Body

{
  "title": "Task Title",
  "description": "Task Description",
  "category": "Task Category",
  "due_date": "YYYY-MM-DD",
  "priority": "High",
  "status": "Pending"
}

Response

{
  "id": "uuid-generated-id",
  "title": "Task Title",
  "description": "Task Description",
  "category": "Task Category",
  "due_date": "YYYY-MM-DD",
  "priority": "High",
  "status": "Pending"
}


GET /tasks/{task_id}
Retrieve a task by its ID.

Response

{
  "id": "task-id",
  "title": "Task Title",
  "description": "Task Description",
  "category": "Task Category",
  "due_date": "YYYY-MM-DD",
  "priority": "High",
  "status": "Pending"
}


PUT /tasks/{task_id}
Update an existing task.

Request Body

{
  "title": "Updated Task Title",
  "description": "Updated Task Description",
  "category": "Updated Category",
  "due_date": "Updated Due Date",
  "priority": "Medium",
  "status": "In Progress"
}

Response

{
  "id": "task-id",
  "title": "Updated Task Title",
  "description": "Updated Task Description",
  "category": "Updated Category",
  "due_date": "Updated Due Date",
  "priority": "Medium",
  "status": "In Progress"
}


DELETE /tasks/{task_id}
Delete a task by its ID.

Response

{
  "message": "Task task-id deleted"
}


Contributing

If you'd like to contribute to the project, follow these steps:

Fork the repository and clone it to your machine:

git clone https://github.com/your-username/task-manager.git
cd task-manager

Create a new branch for your feature or bugfix:

git checkout -b feature-branch

Make your changes, commit them, and push them to your branch:


git commit -am 'Add a new feature or fix a bug'
git push origin feature-branch

Open a pull request to merge your changes into the main branch.


We welcome contributions!

## Demo
Watch a demo of the Task Manager in action: https://youtu.be/CB5FGZRF7JM
