import pymongo
from pymongo import MongoClient
from dotenv import load_dotenv
import os

# load env variable
load_dotenv()
MONGO_DB = os.getenv('MONGO_DB')


cluster = MongoClient(MONGO_DB)
db = cluster.test

collection = db.test


# create POSTS
# POST: {"_id":0, "name": "tom", score: 5} - if id doesn't exist - it is created automatically
post = {"_id": 0, "name": "tom", "score": 5}
collection.insert_one(post)

# close connection
cluster.close()