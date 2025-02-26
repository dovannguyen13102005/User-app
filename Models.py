from pydantic import BaseModel
from Database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Session
from collections import OrderedDict


class User(BaseModel):
    name: str
    age: int
    email: str
    account: str
    password: str

class UserDB(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100), index=True)
    age = Column(Integer, index=True)
    email = Column(String(100), unique=True, index=True)
    account = Column(String(100), unique=True, index=True)
    password = Column(String(100), index=True)


class Users:
    def __init__(self, db: Session):
        self.db = db
    def add_user(self, new_user:User):
        if self.db.query(UserDB).filter(UserDB.email == new_user.email).first():
            return {"Message": "Email existed"}
        if self.db.query(UserDB).filter(UserDB.account == new_user.account).first():
            return {"Message": "Account existed"}
        user = UserDB(**new_user.dict())
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return {"id": user.id, "name": user.name, "age": user.age, "email": user.email, "account": user.account, "password": user.password}
    def get_all_users(self):
        users = self.db.query(UserDB).all()
        return [
            OrderedDict([
                ("id", user.id),
                ("name", user.name),
                ("age", user.age),
                ("email", user.email),
                ("account", user.account),
                ("password", user.password),
            ])
            for user in users
        ]
    def find_user_by_id(self, user_id):
        user = self.db.query(UserDB).filter(UserDB.id == user_id).first()
        if user:
            return {"id": user.id, "name": user.name, "age": user.age, "email": user.email, "account": user.account,"password": user.password}
        else: return {"Message": "Not Found"}
    def find_user_by_email(self, user_email):
        user = self.db.query(UserDB).filter(UserDB.email == user_email).first()
        if user:
            return {"id": user.id, "name": user.name, "age": user.age, "email": user.email, "account": user.account,
                    "password": user.password}
        else:
            return {"Message": "Not Found"}
    def find_user_by_account(self, user_account):
        user = self.db.query(UserDB).filter(UserDB.account == user_account).first()
        if user:
            return {"id": user.id, "name": user.name, "age": user.age, "email": user.email, "account": user.account,
                    "password": user.password}
        else:
            return {"Message": "Not Found"}
    def update_user(self, user_id, new_user:User):
        user = self.db.query(UserDB).filter(UserDB.id == user_id).first()
        if not user:
            return {"Message": "Not Found"}
        if self.db.query(UserDB).filter(UserDB.email == new_user.email).first():
            return {"Message": "Email existed"}
        if self.db.query(UserDB).filter(UserDB.account == new_user.account).first():
            return {"Message": "Account existed"}
        user.name = new_user.name
        user.age = new_user.age
        user.email = new_user.email
        user.account = new_user.account
        user.password = new_user.password
        self.db.commit()
        self.db.refresh(user)
        return {"Message": "Success"}
    def remove_user(self, user_id):
        user = self.db.query(UserDB).filter(UserDB.id == user_id).first()
        if not user:
            return {"Message": "Not Found"}
        self.db.delete(user)
        self.db.commit()
        return {"Message": "Success"}