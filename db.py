import os
from pymongo import MongoClient
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()
MONGO_URI = os.getenv("MONGO_URI")

client = MongoClient(MONGO_URI)
db = client.get_database("bruce_khalawa")
logs = db.get_collection("dm_logs")

def log_message(sender: str, recipient: str, original: str, generated: str) -> bool:
    try:
        log_entry = {
            "sender": sender,
            "recipient": recipient,
            "original_message": original,
            "generated_reply": generated,
            "timestamp": datetime.utcnow()
        }
        result = logs.insert_one(log_entry)
        return result.acknowledged
    except Exception as e:
        print(f"Logging failed: {e}")
        return False
