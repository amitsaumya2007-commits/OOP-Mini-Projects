from enum import Enum
from dataclasses import dataclass
import re

class Role(Enum):
    ADMIN = "admin"
    MEMBER = "member"
    GUEST = "guest"

@dataclass
class User:
    name: str
    email: str
    role:Role = Role.GUEST

    @staticmethod
    def validate_email(email:str):
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        return True if  re.search(pattern,email) else False
    
    @classmethod
    def from_dict(cls, data:dict) -> "User":
        if not cls.validate_email(data["email"]):
            raise ValueError("Invalid email address.")

        else:
         return cls(
            name = data["name"],
            email = data["email"],
            role = Role(data.get("role", "guest")) 
        )

    @classmethod
    def from_json_list(cls, items: list):
        for item in items:
            yield cls.from_dict(item)

    def to_dict(self) -> dict:
        return dict({"name": self.name , "email": self.email, "role": self.role.value })

    @property
    def is_admin(self) -> bool:
        return self.role is Role.ADMIN

raw = [{"name": "Saumya", "email": "s@example.com", "role": "admin"},
        {"name": "Shagun", "email": "shagun@example.com", "role": "guest"},
        {"name": "Sarthak", "email": "sarthak@example.com", "role": "member"},
        {"name": "Krishna", "email": "krish@example.com", "role": "member"}]

gen_obj = User.from_json_list(raw)

for user in gen_obj:
    print(user)