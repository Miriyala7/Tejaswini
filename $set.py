from pymongo import MongoClient

# Assuming you have a MongoClient connected to your MongoDB server
client = MongoClient("mongodb+srv://tejum2108:mine2108@cluster0.1dc7j9s.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client.sample_training
collection = db["zips"]

# Define the aggregation pipeline
pipeline = [
    {
        "$project": {
            "pop_2022": {
                "$round": {
                    "$multiply": [1.0031, "$pop"]
                }
            }
        }
    }
]

# Run the aggregation pipeline
result = list(collection.aggregate(pipeline))

# Print the result or perform further operations
for document in result:
    print(document)