from pydantic import BaseModel, EmailStr, AfterValidator
from typing import Annotated
import re


def check_password(password: str):
    # pattern = re.compile(
    #     r'^(?=.*[a-z])'      # at least one lowercase letter
    #     r'(?=.*[A-Z])'       # at least one uppercase letter
    #     r'(?=.*\d)'          # at least one digit
    #     r'(?=.*[@$!%*?&])'   # at least one special character
    #     r'[A-Za-z\d@$!%*?&]{8,}$'  # allowed chars and min length 8
    # )
    # if (bool(pattern.match(password))):
        return password
    # else :
    #     raise ValueError("invalid password provided")


class LoginDto(BaseModel):
    email: EmailStr
    password: Annotated[str, AfterValidator(check_password)]

class SignupDto(LoginDto):
    age: int
    username: str