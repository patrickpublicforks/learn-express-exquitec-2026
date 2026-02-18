from .env import env

from sqlmodel import SQLModel, create_engine, Session
from src.internal.models.user import User

engine = create_engine(env.DB_URL, echo=env.PY_ENV != "production")


def create_db_and_tables():
    if env.PY_ENV != "production":
        SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session