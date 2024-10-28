from fastapi import FastAPI
from app.core.config import settings

# Create FastAPI instance
app = FastAPI(
    title=settings.PROJECT_NAME,
    description="Back office API for Java Volcano Tour Operator",
    version="1.0.0"
)

# Basic root endpoint
@app.get("/")
def root():
    return {"message": "Welcome to JVTO Back Office API"}

# Simple test endpoint
@app.get("/test")
def test():
    return {"message": "Test endpoint works!"}

# Simple endpoint with parameter
@app.get("/greet/{name}")
def greet(name: str):
    return {"message": f"Hello, {name}!"}