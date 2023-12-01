from app import MongoClient

mongo_client = MongoClient('mongodb://root:example@localhost:27017/')
db = mongo_client['mydatabase']
collection = db['example']
