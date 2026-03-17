from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlmodel import Session, select
from datetime import timedelta


from src.config.db import get_session
from src.internal.models.user import User

from ..dtos.auth_dto import LoginDto, SignupDto
from ..dtos.forgot_password_dto import ForgotPasswordDto, ResetPasswordDto
from ..middlewares.auth_middleware import auth_middleware
from src.config.jwt import create_jwt, verify_jwt

from fastapi.security import APIKeyHeader

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
    
    return user

@app.post("/forgot-password")
def forgot_password(payload: ForgotPasswordDto, session: Session = Depends(get_session)):
    query = select(User).where(User.email == payload.email)
    user = session.exec(query).first()

    # Always return same message (security best practice)
    if not user:
        return {"message": "If this email exists, a reset link has been sent."}

    reset_token = create_jwt(
        {"user_id": user.id, "type": "reset"},
        expires_delta=timedelta(minutes=15)
    )

    # TODO: send via email in production
    return {
        "message": "Reset token generated",
        "reset_token": reset_token
    }

@app.post("/reset-password")
def reset_password(payload: ResetPasswordDto, session: Session = Depends(get_session)):
    try:
        decoded = verify_jwt(payload.token)
    except Exception:
        return JSONResponse(
            status_code=400,
            content={"message": "Invalid or expired token"}
        )

    if decoded.get("type") != "reset":
        return JSONResponse(
            status_code=400,
            content={"message": "Invalid token type"}
        )

    user_id = decoded.get("user_id")

    query = select(User).where(User.id == user_id)
    user = session.exec(query).first()

    if not user:
        return JSONResponse(
            status_code=400,
            content={"message": "User not found"}
        )

    user.password = payload.new_password  # ⚠ hash this later
    session.add(user)
    session.commit()

    return {"message": "Password reset successful"}

@app.get("/user")
def profile(
    user_id: str = Depends(auth_middleware), 
    session: Session = Depends(get_session)
):
    query = select(User).where(User.id == user_id)
    user = session.exec(query).first()

    return user