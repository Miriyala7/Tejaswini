db.zips.aggregate([])



#$group
db.zips.aggregate([{
$group:
{
  _id: "$city",
  totalzips:{$count:{ }}
 }}])
 

#$limit
{$sort:{
   pop: -1
}
},
{$limit:3}

#$project
{ $project: {
state:1,
zip:1,
population:"$pop",
_id:0
}
}

#$set
pop_2022: { $round: { $multiply: [1.0031, "$pop"]}}

#$count
{ $count: "total_zips" }



#$0ut:
  
$group: {
_id:"$state",
total_pop: {$sum:"$pop"}
}
},
{
$match: {
total_pop:{$lt:100000}
}
}
