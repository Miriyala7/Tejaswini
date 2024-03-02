from pymongo import MongoClient

# Assuming you have a MongoClient connected to your MongoDB server
client = MongoClient("mongodb+srv://tejum2108:mine2108@cluster0.1dc7j9s.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client.sample_training
collection = db["zips.aggregate"]

# Define the $project stage
project_stage = {
    "$project": {
        "state": 1,
        "zip": 1,
        "population": "$pop",
        "_id": 0
    }
}

# Run the aggregation pipeline
result = collection.aggregate([project_stage])

# Print the result or perform further operations
for document in result:
    print(document)
