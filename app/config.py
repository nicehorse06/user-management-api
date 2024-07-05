from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv

# 加載 .env 文件中的環境變量
load_dotenv()

MONGO_DETAILS = os.getenv("MONGO_URL", "mongodb://localhost:27017")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = AsyncIOMotorClient(MONGO_DETAILS)
database = client.my_database
user_collection = database.get_collection("users")
