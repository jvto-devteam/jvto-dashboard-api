from fastapi import APIRouter, Query
from typing import Optional

router = APIRouter()

@router.get("/hello/{name}")
async def say_hello(
    name: str,
    greeting: Optional[str] = Query(
        None,
        description="Custom greeting to use",
        example="Hi"
    )
):
    if greeting:
        return {"message": f"{greeting}, {name}!"}
    return {"message": f"Hello, {name}!"}