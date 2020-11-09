import pymongo


class Database:
    DB = None

    @staticmethod
    def initialize():
        client = pymongo.MongoClient('mongodb://127.0.0.1:27017/')
        Database.DB=client.mydb

    @staticmethod
    def insert_record(doc):
        Database.DB.weather.insert_one(doc)

    @staticmethod
    def find_records():
        records = [doc for doc in Database.DB.weather.find({})]
        return records

    @staticmethod
    def delete_all():
        Database.DB.weather.drop()


