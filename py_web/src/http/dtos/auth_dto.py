from pydantic import BaseModel


class LoginDto(BaseModel):
    email: str
    password: str

class SignupDto(LoginDto):
    age: int
    username: str