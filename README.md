🚀 Junior SDE-I Assessment – FastAPI & MongoDB Application

This project implements a FastAPI-based RESTful API that interacts with a local MongoDB database (assessment_db). It supports full CRUD operations and advanced querying features on the employees collection.

⚙️ Technology Stack

Framework: FastAPI

Database: MongoDB (Local)

Database Name: assessment_db

Collection Name: employees

✅ Implemented Features
▶️ Core CRUD Endpoints:

Create Employee – POST /employees

Validates unique employee_id.

Returns 400 on duplicate entries.

Retrieve Employee – GET /employees/{employee_id}

Returns employee details by ID.

Returns 404 if not found.

Update Employee – PUT /employees/{employee_id}

Supports partial field updates.

Returns 404 if employee does not exist.

Delete Employee – DELETE /employees/{employee_id}

Deletes employee record.

Returns appropriate success or failure message.

🔍 Advanced Querying & Aggregation:

Filter by Department – GET /employees?department=Engineering

Retrieves employees from a specific department.

Sorted by joining_date (newest first).

Supports skip and limit for pagination.

Average Salary per Department – GET /employees/avg-salary

Aggregates salary data by department using MongoDB pipeline.

Returns clean, structured response.

Search by Skill – GET /employees/search?skill=Python

Searches employees by skill in their skill set array.

Supports pagination with skip and limit.

✅ Additional Features

Schema validation using Pydantic models

Proper HTTP status codes for errors

Pagination supported everywhere via skip and limit

Indexed employee_id for fast lookups on startup

⚡ Getting Started

Install dependencies in a virtual environment:

python -m venv venv
source venv/bin/activate     # Windows: venv\Scripts\activate
pip install -r requirements.txt


Make sure MongoDB is running on mongodb://localhost:27017/.

Launch the FastAPI server:

uvicorn app.main:app --reload


Access API docs at:
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

🚀 Endpoints Overview
Method	Endpoint	Description
POST	/employees	Add new employee
GET	/employees/{employee_id}	Get employee by ID
PUT	/employees/{employee_id}	Update employee info
DELETE	/employees/{employee_id}	Remove employee
GET	/employees	List employees with filters
GET	/employees/avg-salary	Department-wise average salary
GET	/employees/search	Search by skill