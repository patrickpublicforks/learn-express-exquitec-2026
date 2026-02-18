from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlmodel import Session, select

from src.config.db import get_session
from src.internal.models.user import User

from ..dtos.auth_dto import LoginDto, SignupDto

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
    
    return user

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
    
    return user
