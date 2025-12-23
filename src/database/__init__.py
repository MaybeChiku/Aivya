from motor.motor_asyncio import AsyncIOMotorClient

import config

from .chats import *

# Asynchronous Database Connection
ChatBot = AsyncIOMotorClient(config.MONGO_URL)
# Database
db = ChatBot["Avira"]

# Collections
usersdb = db["users"]  # Users Collection
chatsdb = db["chats"]  # Chats Collection

# Importing other modules
