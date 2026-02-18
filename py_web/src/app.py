from fastapi import FastAPI, Request, Response, status
from fastapi.middleware.cors import CORSMiddleware

from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from contextlib import asynccontextmanager

from .config.db import create_db_and_tables

from .http.controllers.auth import app as authRouter


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield 

app = FastAPI( title= "My Web Project", lifespan=lifespan)

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,            # Allowed origins
    allow_credentials=True,           # Allow cookies/auth headers
    allow_methods=["*"],               # Allow all HTTP methods
    allow_headers=["*"],               # Allow all headers
)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    err =  exc.errors()
    err_message = []
    for e in err:
        err_message .append(f"{e["type"]} {e["loc"][-1]} in {e["loc"][0]} - {e["msg"]}")
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({
            "detail": err_message,
        }),
    )





app.include_router(authRouter)