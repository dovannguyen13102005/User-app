from fastapi import APIRouter, HTTPException
from Users import Users, User

router = APIRouter()
user_manager = Users()

@router.get("/users")
async def get_user():
    return user_manager.get_all_users()
@router.post("/user")
async def create_user(user: User):
    return user_manager.add_user(user)
@router.get("/users/{user_id}")
async def get_user(user_id: int):
    return user_manager.find_user_by_id(user_id)
@router.delete("/user/{user_id}")
async def delete_user(user_id: int):
    return user_manager.remove_user(user_id)