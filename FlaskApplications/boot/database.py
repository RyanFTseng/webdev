import pymongo


class Database:
    DB = None

    @staticmethod
    def initialize():
        client = pymongo.MongoClient('mongodb://127.0.0.1:27017/')
        Database.DB = client.mydb
