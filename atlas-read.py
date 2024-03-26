import pymongo
from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load the environment variable
load_dotenv()
MONGO_DB = os.getenv('MONGO_DB')

# Connect to the MongoDB cluster
cluster = MongoClient(MONGO_DB)

# Select the database and collection
db = cluster.test
collection = db.test

# Fetch all documents from the collection
documents = collection.find()

# Print out each document
for document in documents:
    print(document)

# Close the connection
cluster.close()