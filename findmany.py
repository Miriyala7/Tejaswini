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

    # inserting one account
    documents_to_find = {"college_name": "bvit"}

    # Write an expression that selects the documents matching the query constraint in the 'accounts' collection.
    cursor = college.find(documents_to_find)

    num_docs = 0
    for document in cursor:
        num_docs += 1
        pprint.pprint(document)
        print()
    print("# of documents found: " + str(num_docs))


except Exception as e:
    print(e)
finally:
    client.close()
