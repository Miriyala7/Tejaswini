from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb+srv://tejum2108:mine2108@cluster0.1dc7j9s.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db =client.sample_training
zips_collection = db.zips

# Aggregation pipeline
pipeline = [
    {"$sort": {"pop": -1}},  # Sort documents by the "pop" field in descending order
    {"$limit": 3}  # Limit the result to the top 3 documents
]

# Execute aggregation
result = zips_collection.aggregate(pipeline)

# Print the result
for doc in result:
    print(doc)
