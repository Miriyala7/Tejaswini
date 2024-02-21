from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import datetime
from pprint import pprint

uri = "mongodb+srv://tejum2108:mine2108@cluster0.1dc7j9s.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

try:
    # Send a ping to confirm a successful connection
    client.admin.command('ping')

    # Get reference to 'bank' database
    db = client.universities

    # Get reference to 'accounts' collection
    college= db.college

    # inserting one account
    new_college = {
        "college name": "vishnu institute of technology",
        "college _id": "MDB829001337",
        "college city ": "bhivamaram",
    
    }

    # Write an expression that inserts the 'new_account' document into the 'accounts' collection.
    result = college.insert_one(new_college)

    document_id = result.inserted_id
    pprint(f"_id of inserted document: {document_id}")


except Exception as e:
    print(e)
finally:
    client.close()
