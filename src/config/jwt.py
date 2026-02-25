import jwt
import datetime
from jwt import ExpiredSignatureError, InvalidTokenError
from .env import env
from src.utils.parse_time_string import parse_time_string

def create_jwt(payload: dict) -> str:
    """
    Create a JWT token with an expiration time.
    """
    if not isinstance(payload, dict):
        raise ValueError("Payload must be a dictionary.")

    # Add expiration claim
    payload_copy = payload.copy()
    payload_copy["iat"] = datetime.datetime.now(datetime.timezone.utc)
    payload_copy["exp"] = datetime.datetime.now(datetime.timezone.utc) + parse_time_string(env.JWT_EXPIRY)

    # Encode the token using HS256 algorithm
    token = jwt.encode(payload_copy, env.JWT_SECRET, algorithm="HS256")
    return token

def verify_jwt(token: str) -> dict:
    """
    Verify a JWT token and return its payload if valid.
    """
    try:
        decoded = jwt.decode(token, env.JWT_SECRET, algorithms=["HS256"])
        return decoded
    except ExpiredSignatureError:
        raise ValueError("Token has expired.")
    except InvalidTokenError:
        raise ValueError("Invalid token.")
