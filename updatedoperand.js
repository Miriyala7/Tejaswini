//OPERATORS
//Using Sample_airbnb data

//and logic
db.listingsAndReviews.find({$and: [{amenities: "Wifi"}, {amenities: "TV"}]}); 
