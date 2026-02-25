from dotenv import load_dotenv
load_dotenv()

import uvicorn
import os

def main():
    from src.app import app   # import here to avoid circular import
    uvicorn.run(app, port=int(os.getenv("PORT", 8000)))