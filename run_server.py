#!/usr/bin/env python3
"""
Script to start the FastAPI server with proper configuration.
"""

import uvicorn
import sys
import os

def check_mongodb():
    """Check if MongoDB is accessible"""
    try:
        from app.database import test_connection
        import asyncio
        asyncio.run(test_connection())
        return True
    except Exception as e:
        print(f"❌ MongoDB connection failed: {e}")
        print("Make sure MongoDB is running locally on mongodb://localhost:27017/")
        return False

def main():
    print("🚀 Starting Employee Management API...")
    
    # Check MongoDB connection
    if not check_mongodb():
        sys.exit(1)
    
    print("✅ MongoDB connection successful!")
    print("📖 API documentation will be available at: http://127.0.0.1:8000/docs")
    print("🛑 Press Ctrl+C to stop the server")
    
    # Start the server
    uvicorn.run(
        "app.main:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
        log_level="info"
    )

if __name__ == "__main__":
    main()
