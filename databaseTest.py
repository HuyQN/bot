import pymongo
import hashlib

from pymongo import MongoClient	
from bson.objectid import ObjectId

client = MongoClient('mongodb://localhost:27017/')
testdb = client.testdb

location = testdb.location
commands = testdb.commands

commandtext = "tester"

id = ObjectId(hashlib.md5(commandtext.encode('utf-8')).hexdigest()[:24])
'''text = "testing 123"

command = {'_id': id, 'text': text}

commands.update_one({'_id': id},{"$set": command}, upsert=True)'''

extract = commands.find_one({"_id": id})
print(extract.keys())
#print(extract['item'])