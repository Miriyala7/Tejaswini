from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import datetime

uri = "mongodb+srv://nikshepkulli9:mongodb1234@cluster0.2z6l7np.mongodb.net/?retryWrites=true&w=majority"

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
            
        },
        {
           "college__id": MDB2467899876",
            "college_name": "khit",
            "college_place": "guntur",
              
        },

{
           "college__id": MDB2467896887",
            "college_name": "vvit",
            "college_place": "guntur",
              
        }
    ]

    # Write an expression that inserts the 'new_account' document into the 'accounts' collection.
    result = accounts_collection.insert_many(new_accounts)

    document_ids = result.inserted_ids
    print("# of documents inserted: " + str(len(document_ids)))
    print(f"_ids of inserted documents: {document_ids}")


except Exception as e:
    print(e)
finally:
    client.close()
