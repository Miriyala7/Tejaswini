from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson.objectid import ObjectId
import pprint
uri = "mongodb+srv://tejum2108:mine2108@cluster0.1dc7j9s.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

try:
    # Send a ping to confirm a successful connection
    client.admin.command('ping')

    # Get reference to 'bank' database
    db = client.universities

    # Get reference to 'accounts' collection
    college = db.college

    # Filter
    document_to_update = {"_id": ObjectId("65c2cb3a004800a420ffc3dd")}

    # Update
    add_to_balance = {"$inc": {"college_fee:$800"}}

    # Print original document
    pprint.pprint(college.find_one(document_to_update))

    # Write an expression that adds to the target account balance by the specified amount.
    result = college.update_one(document_to_update)
    print("Documents updated: " + str(result.modified_count))

    # Print updated document
    pprint.pprint(college.find_one(document_to_update))


except Exception as e:
    print(e)
finally:
    client.close()
