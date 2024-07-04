from fastapi import APIRouter, HTTPException
from typing import List
from ..crud import retrieve_user, retrieve_users, add_user
from ..models import User

router = APIRouter()

@router.get("/", response_description="List all users", response_model=List[User])
async def get_users():
    users = await retrieve_users()
    return users

@router.get("/{id}", response_description="Get a single user", response_model=User)
async def get_user(id: str):
    user = await retrieve_user(id)
    if user:
        return user
    raise HTTPException(status_code=404, detail="User not found")

@router.post("/", response_description="Add new user", response_model=User)
async def create_user(user: User):
    new_user = await add_user(user.dict())
    return new_user
