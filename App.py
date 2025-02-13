from fastapi import APIRouter, HTTPException, FastAPI
from fastapi.params import Depends

from Models import Users, User
from fastapi.security import  HTTPBasic, HTTPBasicCredentials

##router = APIRouter()
user_manager = Users()
security = HTTPBasic()
USERNAME = "test"
PASSWORD = "test"

def secure(credentials : HTTPBasicCredentials = Depends(security)):
    if credentials.username == USERNAME and credentials.password == PASSWORD:
        return True
    return False

app = FastAPI()
@app.get("/get_users")
async def get_user(test = Depends(secure)):
    if not test:
        return {"Message": "Can't access"}
    return user_manager.get_all_users()
@app.post("/add_user")
async def create_user(user: User, test = Depends(secure)):
    if not test:
        return {"Message": "Can't access"}
    return user_manager.add_user(user)
@app.get("/find_user_by_id/{user_id}")
async def get_user(user_id: int, test = Depends(secure)):
    if not test:
        return {"Message": "Can't access"}
    return user_manager.find_user_by_id(user_id)
@app.delete("/remove_user/{user_id}")
async def delete_user(user_id: int, test = Depends(secure)):
    if not test:
        return {"Message": "Can't access"}
    return user_manager.remove_user(user_id)
@app.put("/update_user/{user_id}")
async def update_user(user_id: int, user: User, test = Depends(secure)):
    if not test:
        return {"Message": "Can't access"}
    return user_manager.update_user(user_id, user)
@app.get("/find_user_by_name/{user_name}")
async def get_user(user_name: str, test = Depends(secure)):
    if not test:
        return {"Message": "Can't access"}
    return user_manager.find_user_by_name(user_name)
@app.get("/find_user_by_email/{user_email}")
async def get_user(user_email: str, test = Depends(secure)):
    if not test:
        return {"Message": "Can't access"}
    return user_manager.find_user_by_email(user_email)