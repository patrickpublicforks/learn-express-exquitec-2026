import os 
from pydantic import BaseModel


def getenv(val) -> str :
    res = os.getenv(val)
    if res == None:
        raise ValueError(f"cannot find {val} in environmental variables")
    return res

class Env(BaseModel):
    PORT: str =  getenv("PORT")
    PY_ENV: str = getenv("PY_ENV")
    DB_URL: str = getenv("DB_URL")
    JWT_SECRET: str = getenv("JWT_SECRET")
    JWT_EXPIRY: str = getenv("JWT_EXPIRY")



env = Env()