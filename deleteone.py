from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson.objectid import ObjectId
import pprint

uri = "mongodb+srv://nikshepkulli9:mongodb1234@cluster0.2z6l7np.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

try:
    # Send a ping to confirm a successful connection
    client.admin.command('ping')

    # Get reference to 'bank' database
    db = client.univesities

    # Get reference to 'accounts' collection
    college = db.college

    # Filter by ObjectId
    document_to_delete = {"_id": ObjectId("65c2caeaae6140696995984f")}

    # Search for document before delete
    print("Searching for target document before delete: ")
    pprint.pprint(college.find_one(document_to_delete))

    # Write an expression that deletes the target account.
    result = college.delete_one(document_to_delete)

    # Search for document after delete
    print("Searching for target document after delete: ")
    pprint.pprint(college.find_one(document_to_delete))

    print("Documents deleted: " + str(result.deleted_count))


except Exception as e:
    print(e)
finally:
    client.close()
