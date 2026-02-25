import os 
from dotenv import load_dotenv
from pydantic import BaseModel


load_dotenv() 

def getenv(val, default_val=None) -> str :
    res = os.getenv(val)
    if res == None : 
        if default_val != None:
            return default_val
        raise ValueError(f"cannot find {val} in environmental variables") 
    return res

class Env(BaseModel):
    PORT: str =  getenv("PORT", "8000")
    PY_ENV: str = getenv("PY_ENV")
    DB_URL: str = getenv("DB_URL")
    JWT_SECRET: str = getenv("JWT_SECRET")
    JWT_EXPIRY: str = getenv("JWT_EXPIRY")



env = Env()