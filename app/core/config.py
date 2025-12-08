import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    PROJECT_NAME = os.getenv("PROJECT_NAME", "FastAPI Integration Project")
    ENV = os.getenv("ENV", "development")

settings = Settings()
