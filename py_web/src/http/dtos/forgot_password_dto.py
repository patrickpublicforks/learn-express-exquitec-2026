from pydantic import BaseModel, EmailStr

class ForgotPasswordDto(BaseModel):
    email: EmailStr

class ResetPasswordDto(BaseModel):
    token: str
    new_password: str