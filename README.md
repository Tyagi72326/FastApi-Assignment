🚀 Junior SDE-I Assessment – FastAPI & MongoDB Application

This project is a FastAPI-based RESTful API that interacts with a local MongoDB database (assessment_db). It provides full CRUD operations and advanced querying features for managing the employees collection.

⚙️ Technology Stack

Framework: FastAPI

Database: MongoDB (Local)

Database Name: assessment_db

Collection Name: employees

✅ Implemented Features
▶️ Core CRUD Endpoints
Method	Endpoint	Description
POST	/employees	Create new employee. Validates unique employee_id. Returns 400 on duplicate.
GET	/employees/{employee_id}	Retrieve employee by ID. Returns 404 if not found.
PUT	/employees/{employee_id}	Update employee info (partial updates supported). Returns 404 if employee does not exist.
DELETE	/employees/{employee_id}	Delete employee record. Returns appropriate success or failure message.
🔍 Advanced Querying & Aggregation

Filter by Department
GET /employees?department=Engineering
Retrieves employees in a specific department, sorted by joining_date (newest first). Supports pagination via skip and limit.

Average Salary per Department
GET /employees/avg-salary
Returns structured department-wise average salary using MongoDB aggregation pipeline.

Search by Skill
GET /employees/search?skill=Python
Search employees by skill from skills array. Supports pagination via skip and limit.

✅ Additional Features

Schema validation using Pydantic models

Proper HTTP status codes for errors

Pagination supported via skip and limit everywhere

Indexed employee_id for fast lookups on startup

⚡ Getting Started
1️⃣ Setup Virtual Environment and Install Dependencies
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt

2️⃣ Ensure MongoDB is Running

MongoDB should run at:

mongodb://localhost:27017/

3️⃣ Launch FastAPI Server
uvicorn app.main:app --reload

4️⃣ Access API Documentation

Open in browser:
👉 http://127.0.0.1:8000/docs

📄 Sample Employee Document
{
  "employee_id": "E123",
  "name": "John Doe",
  "department": "Engineering",
  "salary": 75000,
  "joining_date": "2023-01-15",
  "skills": ["Python", "MongoDB", "REST APIs"]
}

🚀 Endpoints Summary
Method	Endpoint	Description
POST	/employees	Add new employee
GET	/employees/{employee_id}	Get employee by ID
PUT	/employees/{employee_id}	Update employee info
DELETE	/employees/{employee_id}	Remove employee
GET	/employees	List employees with filters
GET	/employees/avg-salary	Department-wise average salary
GET	/employees/search	Search by skill
