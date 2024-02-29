db.zips.aggregate([])




db.zips.aggregate([{
$group:
{
  _id: "$city",
  totalzips:{$count:{ }}
 }}])
 



{$sort:{
   pop: -1
}
},
{$limit:3}


{ $project: {
state:1,
zip:1,
population:"$pop",
_id:0
}
}


pop_2022: { $round: { $multiply: [1.0031, "$pop"]}}


{ $count: "total_zips" }




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
