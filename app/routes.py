
from fastapi import APIRouter, HTTPException, Query
from .crud import (
    create_employee, get_employee_by_id, update_employee, delete_employee, 
    list_all_employees, list_employees_by_department, get_average_salary_by_department,
    search_employees_by_skill
)
from .models import EmployeeCreate, EmployeeUpdate

router = APIRouter(prefix="/employees", tags=["employees"])

@router.post("/")
async def add_employee(emp: EmployeeCreate):
    try:
        return await create_employee(emp)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/")
async def get_employees(
    department: str = Query(None, description="Filter by department"),
    skip: int = Query(0, ge=0, description="Number of records to skip"),
    limit: int = Query(100, ge=1, le=1000, description="Number of records to return")
):
    if department:
        return await list_employees_by_department(department, skip, limit)
    return await list_all_employees(skip, limit)

@router.get("/{employee_id}")
async def get_employee(employee_id: str):
    emp = await get_employee_by_id(employee_id)
    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")
    return emp

@router.put("/{employee_id}")
async def update_employee_data(employee_id: str, emp: EmployeeUpdate):
    updated = await update_employee(employee_id, emp)
    if not updated:
        raise HTTPException(status_code=404, detail="Employee not found")
    return updated

@router.delete("/{employee_id}")
async def delete_employee_data(employee_id: str):
    success = await delete_employee(employee_id)
    if not success:
        raise HTTPException(status_code=404, detail="Employee not found")
    return {"deleted": success}

@router.get("/avg-salary")
async def get_average_salary():
    """Get average salary grouped by department using MongoDB aggregation"""
    return await get_average_salary_by_department()

@router.get("/search")
async def search_employees(
    skill: str = Query(..., description="Skill to search for"),
    skip: int = Query(0, ge=0, description="Number of records to skip"),
    limit: int = Query(100, ge=1, le=1000, description="Number of records to return")
):
    """Search employees by skill in their skills array"""
    return await search_employees_by_skill(skill, skip, limit)
