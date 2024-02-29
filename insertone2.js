db.details.insertOne({
 "id": "POST_ID",
 "title": "TITLE_OF_POST",
 "description": "POST_DESCRIPTION",
 "by": "POST_BY",
 "url": "URL_OF_POST",
 "tags": ["TAG1", "TAG2", "TAG3"],
 "likes": "TOTAL_LIKES",
 "comments": [
 {
 "user":"COMMENT_BY",
 "message": "TEXT",
 "dateCreated": "DATE_TIME",
 "like": "LIKES"
 },
 {
 "user":"COMMENT_BY",
 "message": "TEXT",
 "dateCreated": "DATE_TIME",
 "like": "LIKES"
 }
 ]
})
