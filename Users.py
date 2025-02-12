from pydantic import BaseModel
from pyexpat.errors import messages


class User(BaseModel):
    name: str
class Users:
    def __init__(self):
        self.users = []
        self.cnt = 1
    def get_all_users(self):
        return self.users
    def add_user(self, user: User):
        new_user = {"id": self.cnt, "name": user.name}
        self.users.append(new_user)
        self.cnt += 1
        return new_user
    def find_user_by_id(self, user_id: int):
        for user in self.users:
            if user["id"] == user_id:
                return user
        return {"Message", "Not Found"}
    def remove_user(self, user_id: int):
        for user in self.users:
            if user["id"] == user_id:
                self.users.remove(user)
                return {"Messages", "User deleted"}
        return {"Message", "Not Found"}
