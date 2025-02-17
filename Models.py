from pydantic import BaseModel
from pyexpat.errors import messages


class User(BaseModel):
    name: str
    age: int
    email: str
    account: str
    password: str

class NewUser:
    def __init__(self, user_id, user_name, user_age, user_email, user_account, user_password):
        self.user_id = user_id
        self.user_name = user_name
        self.user_age = user_age
        self.user_email = user_email
        self.user_account = user_account
        self.user_passWord = user_password
class Users:
    def __init__(self):
        self.users = list()
        self.check_existed = dict()
        self.count = 1
    def add_user(self, new_user:User):
        temp_user = NewUser(self.count, new_user.name, new_user.age, new_user.email, new_user.account, new_user.password)
        if self.check_existed.get(new_user.account):
            return {"Message": "Account existed"}
        if self.check_existed.get(new_user.email):
            return {"Message": "Email existed"}
        self.users.append(temp_user)
        self.check_existed[new_user.email] = True
        self.check_existed[new_user.account] = True
        self.count += 1
        return temp_user
    def get_all_users(self):
        return self.users
    def find_user_by_id(self, user_id):
        for user in self.users:
            if user.user_id == user_id:
                return user
        return {"Message": "Not Found"}
    def find_user_by_email(self, user_email):
        for user in self.users:
            if user.user_email == user_email:
                return user
        return {"Message": "Not Found"}
    def find_user_by_account(self, user_account):
        for user in self.users:
            if user.user_account == user_account:
                return user
        return {"Message": "Not Found"}
    def update_user(self, user_id, new_user:User):
        temp_user = NewUser(user_id, new_user.name, new_user.age, new_user.email, new_user.account, new_user.password)
        if self.check_existed.get(new_user.account):
            return {"Message": "Account existed"}
        for idx,user in enumerate(self.users):
            if user.user_id == user_id:
                self.users[idx] = temp_user
                return {"Message": "Success"}
        return {"Message": "Not Found"}
    def remove_user(self, user_id):
        for user in self.users:
            if user.user_id == user_id:
                self.users.remove(user)
                return {"Message": "Success"}
        return {"Message": "Not Found"}