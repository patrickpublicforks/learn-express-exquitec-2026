from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlmodel import Session, select

from src.config.db import get_session
from src.models.user import User


from ..dtos.auth_dto import LoginDto, SignupDto
from ..middlewares.auth_middleware import auth_middleware
from src.config.jwt import create_jwt

from fastapi.security import APIKeyHeader
from datetime import datetime, timedelta

from fastapi import HTTPException



app = APIRouter( tags=["AUTH"])



@app.post("/login")
def login(payload: LoginDto, session: Session = Depends(get_session)):
    query = select(User).where(User.email == payload.email)
    user = session.exec(query).first()

    if user == None:
        return JSONResponse(
            status_code=400,
            content={
                "message": "invalid email/password"
            }
        )
    
    if user.password != payload.password:
        return JSONResponse(
            status_code=400,
            content={
                "message": "invalid email/password"
            }
        )
    
    token = create_jwt({ "user_id" : user.id })
    return { "token": token }

@app.post("/signup")
def signup(payload: SignupDto, session: Session = Depends(get_session)):
    query = select(User).where(User.email == payload.email)
    user = session.exec(query).first()

    if user != None:
        return JSONResponse(
            status_code=400,
            content={
                "message": "user already exist please login"
            }
        )
    
    user = User(age = payload.age, email=payload.email, password=payload.password, username=payload.username)
    session.add(user)
    session.commit()
    session.refresh(user)

    access_token = create_jwt({
        "sub": str(user.id)
    })

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user": {
            "id": user.id,
            "email": user.email,
            "username": user.username,
            "age": user.age
        }
    }

@app.get("/user")
def profile(
    user_id: str = Depends(auth_middleware), 
    session: Session = Depends(get_session)
):
    query = select(User).where(User.id == user_id)
    user = session.exec(query).first()

    return user

