from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import datetime
import pprint

uri = "mongodb+srv://tejum2108:mine2108@cluster0.1dc7j9s.mongodb.net"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

try:
    # Send a ping to confirm a successful connection
    client.admin.command('ping')

    # Get reference to 'bank' database
   


except Exception as e:
    print(e)

    
    
db = client.sample_resturant

# Get reference to 'accounts' collection
indian_collection  = db.resturants

    # inserting one account
new_resturant = {
        "Resturant_place": "vijayawada",
        "Resturant _id": "MDB829001337",

        "Rating": 5,
}

    # Write an expression that inserts the 'new_account' document into the 'accounts' collection.
result = indian_collection.insert_one(new_resturant)

document_id = result.inserted_id
print(document_id)




 # inserting many accounts
new_accounts = [
        {
            "resturant_id": "MDB67892545",
            "resturanr_place": "chennai",
            "rating": 4.0
        },
        {
            "resturant_id": "MDB829000001",
            "resturant_place": "mumbai",
            "rating": 2.1,
        },
    ]

    # Write an expression that inserts the 'new_account' document into the 'accounts' collection.
result = indian_collection.insert_many(new_accounts)

document_ids = result.inserted_ids
print("# of documents inserted: " + str(len(document_ids)))
print(f"_ids of inserted documents: {document_ids}") 
