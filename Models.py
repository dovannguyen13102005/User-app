from pydantic import BaseModel
from pyexpat.errors import messages


class User(BaseModel):
    name: str
    age: int
    email: str
    account: str
    password: str

class Users:
    def __init__(self):
        self.users = []
        self.cnt = 1
    def get_all_users(self):
        return self.users
    def add_user(self, user: User):
        new_user = {"id": self.cnt, "name": user.name, "age": user.age,"email": user.email, "account": user.account, "password": user.password}
        if any(value["account"] == user.account for value in self.users):
            return {"Message": "Account already exists"}
        self.users.append(new_user)
        self.cnt += 1
        return new_user
    def update_user(self, user_id: int, user: User):
        new_user = {"id": user_id, "name": user.name, "age": user.age, "email": user.email}
        for idx, value in enumerate(self.users):
            if value["id"] == user_id:
                self.users[idx] = new_user
                return {"Message": "Success"}
        return {"Message", "Error"}
    def find_user_by_id(self, user_id: int):
        for user in self.users:
            if user["id"] == user_id:
                return user
        return {"Message": "Not Found"}
    def find_user_by_name(self, user_account: str):
        for user in self.users:
            if user["account"] == user_account:
                return user
        return {"Message": "Not Found"}
    def find_user_by_email(self, user_email: str):
        for user in self.users:
            if user["email"] == user_email:
                return user
            return {"Message": "Not Found"}
    def remove_user(self, user_id: int):
        for user in self.users:
            if user["id"] == user_id:
                self.users.remove(user)
                return {"Messages": "User deleted"}
        return {"Message": "Not Found"}
