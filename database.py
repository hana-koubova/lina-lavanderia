import os
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import certifi

uri = os.environ.get('MONGO_URI')

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'), tlsCAFile=certifi.where())

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client['users']
user_companies = db['user_companies']
admins = db['admins']
legals = db['legals']