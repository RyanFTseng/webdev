import pymongo


class Database:
    DB = None

    @staticmethod
    def initialize():
        client = pymongo.MongoClient('mongodb://127.0.0.1:27017/')
        Database.DB = client.mydb

    @staticmethod
    def signup(username, password, email):
        Database.DB.users.insert_one({'username': username, 'password': password, 'email': email})

    @staticmethod
    def find_records():
        records = [doc for doc in Database.DB.users.find({})]
        return records

    @staticmethod
    def login(username, password):
        record = Database.DB.users.find({'username': username}, {'password': password})
        return record

    @staticmethod
    def clear():
        Database.DB.users.drop()

    @staticmethod
    def find_one(doc):
        return Database.DB.users.find_one(doc)
