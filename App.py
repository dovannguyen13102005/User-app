from fastapi import APIRouter, HTTPException, FastAPI
from fastapi.params import Depends
from sqlalchemy.orm import Session

from Models import Users, User, UserDB
from fastapi.security import  HTTPBasic, HTTPBasicCredentials
from Database import Base, engine, SessionLocal

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

Base.metadata.create_all(bind=engine)

security = HTTPBasic()
USERNAME = "test"
PASSWORD = "test"

def secure(credentials : HTTPBasicCredentials = Depends(security)):
    if credentials.username == USERNAME and credentials.password == PASSWORD:
        return True
    return False

app = FastAPI()
@app.get("/get_users")
async def get_user(test = Depends(secure), db: Session = Depends(get_db)):
    if not test:
        return {"Message": "Can't access"}
    user_manager = Users(db)
    return user_manager.get_all_users()
@app.post("/add_user")
async def create_user(user: User, test = Depends(secure), db: Session = Depends(get_db)):
    if not test:
        return {"Message": "Can't access"}
    user_manager = Users(db)
    return user_manager.add_user(user)
@app.get("/find_user_by_id/{user_id}")
async def get_user(user_id: int, test = Depends(secure), db: Session = Depends(get_db)):
    if not test:
        return {"Message": "Can't access"}
    user_manager = Users(db)
    return user_manager.find_user_by_id(user_id)
@app.delete("/remove_user/{user_id}")
async def delete_user(user_id: int, test = Depends(secure), db: Session = Depends(get_db)):
    if not test:
        return {"Message": "Can't access"}
    user_manager = Users(db)
    return user_manager.remove_user(user_id)
@app.put("/update_user/{user_id}")
async def update_user(user_id: int, user: User, test = Depends(secure), db: Session = Depends(get_db)):
    if not test:
        return {"Message": "Can't access"}
    user_manager = Users(db)
    return user_manager.update_user(user_id, user)
@app.get("/find_user_by_account/{user_account}")
async def get_user(user_account: str, test = Depends(secure), db: Session = Depends(get_db)):
    if not test:
        return {"Message": "Can't access"}
    user_manager = Users(db)
    return user_manager.find_user_by_account(user_account)
@app.get("/find_user_by_email/{user_email}")
async def get_user(user_email: str, test = Depends(secure), db: Session = Depends(get_db)):
    if not test:
        return {"Message": "Can't access"}
    user_manager = Users(db)
    return user_manager.find_user_by_email(user_email)