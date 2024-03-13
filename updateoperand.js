//OPERATORS

//and logic
db.listingsAndReviews.find({$and: [{amenities: "Wifi"}, {amenities: "TV"}]}); 

@@ -28,8 +30,8 @@ db.grades.find({ _id: ObjectId("65b9b6f769c4895078585dc0") })
db.listingsAndReviews.find({amenities: "Wifi"});

//insertOne() 
db.CreateColelction("SHU")
db.SHU.insertOne({
db.CreateColelction("Student")
db.Student.insertOne({
  student_id: 654321,
  products: [
    {
@@ -54,7 +56,7 @@ db.SHU.insertOne({


//insertMany()
db.SHU.insertMany([
db.Student.insertMany([
  {
    student_id: 546789,
    products: [
@@ -125,16 +127,16 @@ db.SHU.insertMany([


//lesserthan
db.SHU.find({ "products.score": { $lt: 59  } })
db.Student.find({ "products.score": { $lt: 59  } })

//lesserthanequalto
db.SHU.find({ "products.score": { $lte: 58  } })
db.Student.find({ "products.score": { $lte: 58  } })

//greaterthan
db.SHU.find({ "products.score: { $gt:59  } })
db.Student.find({ "products.score: { $gt:59  } })
//greaterthanequalto
db.SHU.find({ "products.score": { $lt: 59  } })
db.Student.find({ "products.score": { $lt: 59  } })
//in
db.grades.find({ student_id: { $in: [654321, 546789] } })
@@ -144,19 +146,19 @@ db.grades.find({ _id: { $in: [ObjectId('65b9b75969c4895078585dc1'), ObjectId('65
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = mongodb+srv://tejum2108:<password>@cluster0.1dc7j9s.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0

# Create a new client and connect to the server
//Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
// Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
    '''for db_name in client.list_database_names():
        print(db_name)*/''' #once sucessfully established connection
except Exception as e:

output:
PS'C:\Users\tejas\AppData\Local\Programs\Python\Python312\python.exe"c:/Users/hp/OneDrive/Desktop/Adv Data Base design/mangodb python.py"
Pinged your deployment. You successfully connected to MongoDB!
Pinged your deployment. You successfully connected to MongoDB! */


                                                    
