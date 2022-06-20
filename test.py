
from pymongo import MongoClient,InsertOne
from bson.objectid import ObjectId

import pprint

user={
        "id":"123546466",
        "name":"test user",
        "email":"test@example.com",
    }
print("1) Insert user into database")
print("2) Read user into database")

print("3) Update user into database")
print("4) Delete user into database")

choice=int(input("Enter your choice"))
def read_user():
    client=MongoClient('localhost', 27017)
    db=client["test"]
    collection=db['users']
    pp=pprint.PrettyPrinter(indent=2,width=100)
    for x in collection.find():
        pp.pprint(x)
        


def insert_user(user):
    client=MongoClient('localhost', 27017)
    db=client["test"]
    collection=db['users']
    
    user_id=collection.insert_one(user).inserted_id
    print(user_id)
    return user_id

def update_user(name):
    newName=input("please enter new name of the user")
    client=MongoClient('localhost', 27017)
    db=client["test"]
    collection=db['users']
    collection.update_one({"name":name},{"$set":{"name":newName}})

def delete_user(email):
    client=MongoClient('localhost', 27017)
    db=client["test"]
    collection=db['users']
    collection.delete_one({"email":email})


if choice == 1:
    user_id=insert_user(user)
elif choice == 2:
    read_user()
elif choice == 3:
    name=input("Enter name of user to update")
    update_user(name)
elif choice == 4:
    email=input("Enter name of user to delete")
    delete_user(email)

else:
    print("invalid choice")