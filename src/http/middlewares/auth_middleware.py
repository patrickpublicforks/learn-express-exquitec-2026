from typing import Optional
from src.config.jwt import  verify_jwt
from fastapi import HTTPException, Depends
from fastapi.security import APIKeyHeader

authorization = APIKeyHeader(name="authorization",scheme_name="authorization",)

def auth_middleware(token: str =  Depends(authorization)):
    # token: Optional[str] = request.headers.get("authorization")

    if (token == None):
        raise HTTPException(status_code=4011, detail="unauthorized")
    
    token = token.split(" ")[-1]

    try:
        payload =  verify_jwt(token)
    except ValueError as e:
        print("Error Authorizing user", e)
        raise HTTPException(status_code=401, detail="unauthorized")
    
    user_id: Optional[str] = payload.get("user_id")

    if (user_id == None):
        raise HTTPException(status_code=401, detail="unauthorized")
        
    return user_id
