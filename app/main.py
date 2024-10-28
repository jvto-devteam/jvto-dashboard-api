from fastapi import FastAPI
from app.core.config import settings

# Create FastAPI application instance
app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# Define root endpoint
@app.get("/")
def root():
    return {"message": "Welcome to JVTO Back Office API"}