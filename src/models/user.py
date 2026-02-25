# from datetime import datetime
from typing import Optional
from sqlmodel import Field, SQLModel

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    email: str
    password: str
    username: str
    age: Optional[int] = None

    # otp_code: Optional[str] = None
    # otp_expiry: Optional[datetime] = None

    


    