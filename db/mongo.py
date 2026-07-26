import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()


class MongoDB:

    def __init__(self):
        self.enabled = False

        use_mongo = os.getenv("USE_MONGO", "false").lower() == "true"

        if not use_mongo:
            return

        env = os.getenv("ENVIRONMENT", "local")

        uri = {
            "docker": os.getenv("MONGO_URI_DOCKER"),
            "local": os.getenv("MONGO_URI_LOCAL")
        }.get(env)

        db_name = os.getenv("MONGO_DB", "default_db")

        self.client = MongoClient(uri)
        self.db = self.client[db_name]
        self.collection = self.db["challenge_five"]
        self.enabled = True

    def insert(self, data: dict):
        if not self.enabled:
            return None

        return self.collection.insert_one(data)