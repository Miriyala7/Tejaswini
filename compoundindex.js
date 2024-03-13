db.student.createIndex({student_id: 777777, student_id: 223344},
{
			"createdCollectionAutomatically": false,
			"numIdexesBefore":1,
			"numIndexesAfter":2,
			"ok":1
})

output:
student_id_223344

db.student.getIndexes()
  
output:[
  { v: 2, key: { _id: 1 }, name: '_id_' },
  { v: 2, key: { class_id: 551 }, name: 'class_id_551' },
  { v: 2, key: { student_id: 223344 }, name: 'student_id_223344' }
]

