import os
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import certifi

uri = 'mongodb+srv://koubovahan:w6yztr7GMlF1Yh4A@cluster0.x92st.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0' #os.environ.get('MONGO_URI')

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'), tlsCAFile=certifi.where())

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client['users']
pre_approve = db['pre_approve']
user_companies = db['user_companies']