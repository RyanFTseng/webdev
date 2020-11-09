import pymongo


class Database:
    DB = None

    @staticmethod
    def initialize():
        client = pymongo.MongoClient('mongodb://127.0.0.1:27017/')
        Database.DB=client.mydb

    @staticmethod
    def insert_record(doc):
        Database.DB.users.insert_one(doc)

    @staticmethod
    def find_records():
        records = [doc for doc in Database.DB.users.find({})]
        return records

    @staticmethod
    def delete_all():
        Database.DB.users.drop()

    @staticmethod
    def delete_one(doc):
        Database.DB.users.delete_one(doc)

    @staticmethod
    def edit_record(args,doc):
        Database.DB.users.update_one(args,{'$set':doc})

