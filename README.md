django chat API
===================

These are the three API's for the following purpose
- Get all users order by most recent conversation with information of last message
    http://localhost/
- Send message to the other user,
    http://127.0.0.1:8000/sendmessage/
with post data={'message': 'message', 'sender_id': 2, 'receiver_id': 3}
- Get conversations between two users.
    http://localhost/getconv/user1_id/user2_id
    e.g. http://127.0.0.1:8000/getconv/2/7/
    


