import pymongo
from configs import DB_URI, DB_NAME

client = pymongo.MongoClient(DB_URI)
db = client[DB_NAME]
users_collection = db["users"]

async def add_user(user_id: int):
    users_collection.update_one({"user_id": user_id}, {"$set": {"user_id": user_id}}, upsert=True)

async def del_user(user_id: int):
    users_collection.delete_one({"user_id": user_id})

async def full_userbase():
    return [doc["user_id"] for doc in users_collection.find()]

async def present_user(user_id: int):
    return users_collection.find_one({"user_id": user_id}) is not None