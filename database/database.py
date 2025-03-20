from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient
import os

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
DATABASE_NAME = os.getenv("DB_NAME")

client = AsyncIOMotorClient(MONGO_URI)
db = client[DATABASE_NAME]
jobs_collection = db["jobs"]
