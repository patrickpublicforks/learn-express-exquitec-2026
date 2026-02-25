from .env import env
from sqlmodel import SQLModel, create_engine, Session

# Use ONE engine only
engine = create_engine(
    env.DB_URL, 
    echo=env.PY_ENV != "production"
)


def get_session():
    with Session(engine) as session:
        yield session