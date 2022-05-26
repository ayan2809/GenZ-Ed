from pymongo import MongoClient
import environ
env = environ.Env()
environ.Env.read_env()

password=env('mongo_password')


class Connect(object):
    @staticmethod    
    def get_connection():
        return MongoClient('mongodb+srv://ayan:'+password+'@cluster0.ii6mh.mongodb.net/?retryWrites=true&w=majority')