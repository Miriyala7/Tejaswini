from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb+srv://tejum2108:mine2108@cluster0.1dc7j9s.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client.your_database_name
zips_collection = db.zips
# Aggregation pipeline
pipeline = [
    {
        "$group": {
            "_id": "$city",
            "totalzips": {"$sum": 1}  # Count the number of documents (ZIP codes) for each city
        }
    }
]

# Execute aggregation
result = zips_collection.aggregate(pipeline)

# Print the result
for doc in result:
    print(doc)
