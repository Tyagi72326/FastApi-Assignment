
from .database import get_collection
from .models import EmployeeCreate, EmployeeUpdate
from typing import Optional, List, Dict, Any

COLLECTION_NAME = "employees"

async def create_index_if_not_exists():
    coll = get_collection(COLLECTION_NAME)
    await coll.create_index('employee_id', unique=True)

async def create_employee(emp: EmployeeCreate) -> Dict[str, Any]:
    coll = get_collection(COLLECTION_NAME)
    doc = emp.dict()
    if hasattr(doc['joining_date'], 'isoformat'):
        doc['joining_date'] = doc['joining_date'].isoformat()
    
    # Check if employee_id already exists
    existing = await coll.find_one({'employee_id': doc['employee_id']})
    if existing:
        raise ValueError(f"Employee with ID {doc['employee_id']} already exists")
    
    await coll.insert_one(doc)
    return doc

async def get_employee_by_id(employee_id: str) -> Optional[Dict[str, Any]]:
    coll = get_collection(COLLECTION_NAME)
    return await coll.find_one({'employee_id': employee_id})

async def update_employee(employee_id: str, update_data: EmployeeUpdate) -> Optional[Dict[str, Any]]:
    coll = get_collection(COLLECTION_NAME)
    payload = {k: v for k, v in update_data.dict().items() if v is not None}
    if 'joining_date' in payload and hasattr(payload['joining_date'], 'isoformat'):
        payload['joining_date'] = payload['joining_date'].isoformat()
    if not payload:
        return await coll.find_one({'employee_id': employee_id})
    await coll.update_one({'employee_id': employee_id}, {'$set': payload})
    return await coll.find_one({'employee_id': employee_id})

async def delete_employee(employee_id: str) -> bool:
    coll = get_collection(COLLECTION_NAME)
    result = await coll.delete_one({'employee_id': employee_id})
    return result.deleted_count == 1

async def list_all_employees(skip: int = 0, limit: int = 100) -> List[Dict[str, Any]]:
    coll = get_collection(COLLECTION_NAME)
    return [doc async for doc in coll.find().skip(skip).limit(limit)]

async def list_employees_by_department(department: str, skip: int = 0, limit: int = 100) -> List[Dict[str, Any]]:
    """List employees by department, sorted by joining_date (newest first)"""
    coll = get_collection(COLLECTION_NAME)
    cursor = coll.find({"department": department}).sort("joining_date", -1).skip(skip).limit(limit)
    return [doc async for doc in cursor]

async def get_average_salary_by_department() -> List[Dict[str, Any]]:
    """Use MongoDB aggregation to compute average salary grouped by department"""
    coll = get_collection(COLLECTION_NAME)
    pipeline = [
        {
            "$group": {
                "_id": "$department",
                "avg_salary": {"$avg": "$salary"}
            }
        },
        {
            "$project": {
                "_id": 0,
                "department": "$_id",
                "avg_salary": {"$round": ["$avg_salary", 2]}
            }
        },
        {
            "$sort": {"department": 1}
        }
    ]
    return [doc async for doc in coll.aggregate(pipeline)]

async def search_employees_by_skill(skill: str, skip: int = 0, limit: int = 100) -> List[Dict[str, Any]]:
    """Search employees who have the given skill in their skills array"""
    coll = get_collection(COLLECTION_NAME)
    cursor = coll.find({"skills": skill}).skip(skip).limit(limit)
    return [doc async for doc in cursor]
