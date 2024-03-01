from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb+srv://tejum2108:mine2108@cluster0.1dc7j9s.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client.your_database_name
collection = db.zips


pipeline = [
    {
        "$group": {
            "_id": "$city",
            "totalzips": {"$sum": 1}  # Counting the number of documents in each group
        }
    }
]

# Run aggregation
result = collection.aggregate(pipeline)

# Print the result
for document in result:
    print(document)
