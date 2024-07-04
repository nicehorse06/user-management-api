from .config import user_collection
from .models import User
from bson.objectid import ObjectId
from fastapi import HTTPException

def user_helper(user) -> dict:
    return {
        "id": str(user["_id"]),
        "name": user["name"],
        "email": user["email"],
        "age": user["age"],
    }

async def retrieve_user(id: str) -> User:
    try:
        oid = ObjectId(id)
    except Exception:
        raise HTTPException(status_code=404, detail="User not found")
    
    user = await user_collection.find_one({"_id": oid})
    if user:
        return User(**user_helper(user))
    raise HTTPException(status_code=404, detail="User not found")

async def retrieve_users():
    users = []
    async for user in user_collection.find():
        users.append(User(**user_helper(user)))
    return users

async def add_user(user_data: dict) -> User:
    user_data = {k: v for k, v in user_data.items() if v is not None}
    user = await user_collection.insert_one(user_data)
    new_user = await user_collection.find_one({"_id": user.inserted_id})
    return User(**user_helper(new_user))
