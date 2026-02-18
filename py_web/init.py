from dotenv import load_dotenv;load_dotenv()
import  uvicorn, os

from src.app import app

def main():
    uvicorn.run(app, port=int(os.getenv("PORT")))
