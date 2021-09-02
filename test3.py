from config import db

# test for database access

#db.users.insert_one({"name": "Corey", "email": "test@gmail.com"})
#db.users.insert_one({"name": "Admin", "email": "admin@gmail.com"})
#db.users.insert_one({"name": "Staff", "email": "staff@gmail.com"})


cursor = db.users.find({"name": "Staff"})
for user in cursor:
    print(user)