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
        self.count = 0
    def add_user(self, user:User):
        new_user = NewUser(self.count, user.name, user.age, user.email, user.account, user.password)
        if self.check_existed[user.account]:
            return {"Message": "existed"}
        self.users.append(new_user)
        self.check_existed[user.account] = True
        self.count += 1
        return user
    def find_user_by_id(self, user_id):
        for value in self.users:
            value.
