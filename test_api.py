#!/usr/bin/env python3
"""
Simple test script to verify the API endpoints work correctly.
Run this after starting the FastAPI server.
"""

import requests
import json
from datetime import date

BASE_URL = "http://127.0.0.1:8000"

def test_api():
    print("🧪 Testing Employee Management API...")
    
    # Test data
    test_employee = {
        "employee_id": "E001",
        "name": "John Doe",
        "department": "Engineering",
        "salary": 75000,
        "joining_date": "2023-01-15",
        "skills": ["Python", "MongoDB", "APIs"]
    }
    
    test_employee2 = {
        "employee_id": "E002",
        "name": "Jane Smith",
        "department": "Engineering",
        "salary": 80000,
        "joining_date": "2023-02-01",
        "skills": ["Python", "React", "Docker"]
    }
    
    test_employee3 = {
        "employee_id": "E003",
        "name": "Bob Johnson",
        "department": "HR",
        "salary": 60000,
        "joining_date": "2023-01-20",
        "skills": ["Python", "Excel", "Communication"]
    }
    
    try:
        # Test 1: Create employees
        print("\n1. Creating employees...")
        for emp in [test_employee, test_employee2, test_employee3]:
            response = requests.post(f"{BASE_URL}/employees", json=emp)
            print(f"   Created {emp['name']}: {response.status_code}")
        
        # Test 2: Get employee by ID
        print("\n2. Getting employee by ID...")
        response = requests.get(f"{BASE_URL}/employees/E001")
        print(f"   Get E001: {response.status_code}")
        if response.status_code == 200:
            print(f"   Data: {response.json()['name']}")
        
        # Test 3: List all employees
        print("\n3. Listing all employees...")
        response = requests.get(f"{BASE_URL}/employees")
        print(f"   Status: {response.status_code}")
        print(f"   Count: {len(response.json())}")
        
        # Test 4: Filter by department
        print("\n4. Filtering by department (Engineering)...")
        response = requests.get(f"{BASE_URL}/employees?department=Engineering")
        print(f"   Status: {response.status_code}")
        print(f"   Engineering employees: {len(response.json())}")
        
        # Test 5: Average salary by department
        print("\n5. Getting average salary by department...")
        response = requests.get(f"{BASE_URL}/employees/avg-salary")
        print(f"   Status: {response.status_code}")
        if response.status_code == 200:
            for dept in response.json():
                print(f"   {dept['department']}: ${dept['avg_salary']}")
        
        # Test 6: Search by skill
        print("\n6. Searching by skill (Python)...")
        response = requests.get(f"{BASE_URL}/employees/search?skill=Python")
        print(f"   Status: {response.status_code}")
        print(f"   Python developers: {len(response.json())}")
        
        # Test 7: Update employee
        print("\n7. Updating employee...")
        update_data = {"salary": 85000}
        response = requests.put(f"{BASE_URL}/employees/E001", json=update_data)
        print(f"   Update E001: {response.status_code}")
        
        # Test 8: Pagination
        print("\n8. Testing pagination...")
        response = requests.get(f"{BASE_URL}/employees?limit=2")
        print(f"   Status: {response.status_code}")
        print(f"   Limited to 2: {len(response.json())}")
        
        # Test 9: Delete employee
        print("\n9. Deleting employee...")
        response = requests.delete(f"{BASE_URL}/employees/E003")
        print(f"   Delete E003: {response.status_code}")
        
        print("\n✅ All tests completed!")
        
    except requests.exceptions.ConnectionError:
        print("❌ Could not connect to the API. Make sure the server is running on http://127.0.0.1:8000")
    except Exception as e:
        print(f"❌ Error during testing: {e}")

if __name__ == "__main__":
    test_api()
