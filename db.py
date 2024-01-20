from datetime import datetime
from bson import ObjectId
from pymongo import MongoClient
from werkzeug.security import generate_password_hash
from user import User

client = MongoClient("mongodb+srv://saurabhvishwakarma:Vishwakarma^(755)@cluster0.pje6o0d.mongodb.net/?retryWrites=true&w=majority")

chat_db = client.get_database("ChatDB")
user_collection = chat_db.get_collection("users")
room_collection = chat_db.get_collection("rooms")
room_member_collection = chat_db.get_collection("room_members")

def save_user(username, email, password):
    password_hash = generate_password_hash(password)
    user_collection.insert_one({'_id':username, 'email':email, 'password':password_hash})

def get_user(username):
    user_data = user_collection.find_one({'_id':username})
    return User(user_data['_id'], user_data['email'], user_data['password']) if user_data else None

def save_room(room_name, create_by):
    room_id = room_collection.insert_one(
        {
            "name":room_name,
            "create_by":create_by,
            "created_at":datetime.now()
        }
    ).inserted_id
    add_room_member(room_id, room_name, create_by, create_by, is_room_admin=True)
    return room_id


def update_roon(room_id, room_name):
    room_collection.update_one({'_id':ObjectId(room_id)}, {'$set':{'name':room_name}})
    room_member_collection.update_many({'_id.room_id': ObjectId(room_id)}, {'$set': {'room_name':room_name}})

def get_room(room_id):
    return room_collection.find_one({'_id': ObjectId(room_id)})

def add_room_member(room_id, room_name, username, added_by, is_room_admin=False):
    room_member_collection.insert_one(
        {
            '_id': {
                'room_id': ObjectId(room_id),
                'username': username
                  },
            'room_name': room_name,
            'added_by': added_by,
            'added_at': datetime.now(),
           'is_room_admin': is_room_admin
        }
    )

def add_room_members(room_id, room_name, usernames, added_by):
    room_member_collection.insert_many(
        [
            {
                '_id': {
                    'room_id': ObjectId(room_id),
                    'username': username
                    },
                'room_name': room_name,
                'added_by': added_by,
                'added_at': datetime.now(),
                'is_room_admin': False
            } 
            for username in usernames
        ]
    )


def remove_room_members(room_id, usernames):
    room_member_collection.delete_many({'_id': {'$in': [{'room_id':room_id, 'username':username} for username in usernames]}})

def get_room_members(room_id):
    return list(room_member_collection.find({'_id.room_id': ObjectId(room_id)}))

def get_rooms_for_user(username):
    return list(room_member_collection.find({'_id.username' : username}))

def is_room_member(room_id, username):
    return room_member_collection.count_documents({'_id': {'room_id': ObjectId(room_id), 'username': username}})

def is_room_admin(room_id, username):
    return room_member_collection.count_documents(
        {'_id': {'room_id': ObjectId(room_id), 'username': username}, 'is_room_admin': True})