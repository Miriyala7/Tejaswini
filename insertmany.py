from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import datetime

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

    # inserting many accounts
    new_college = [
        {
            "college__id": "MDB011235813",
            "college_name": "bvit",
            "college_place": "bhimavaram",
            "college_fee":"$800",
        },
        {
           "college__id": "MDB2467899876",
            "college_name": "khit",
            "college_place": "guntur",
            "college_fee":"$700",
              
        },

{
           "college__id": "MDB2467896887",
            "college_name": "vvit",
            "college_place": "guntur",
            "college_fee":"$900",
        }
    ]

    # Write an expression that inserts the 'new_account' document into the 'accounts' collection.
    result = college.insert_many(new_college)

    document_ids = result.inserted_ids
    print("# of documents inserted: " + str(len(document_ids)))
    print(f"_ids of inserted documents: {document_ids}")


except Exception as e:
    print(e)
finally:
    client.close()
