import pymongo
import hashlib

from pymongo import MongoClient
from bson.objectid import ObjectId

localdb = 'mongodb://localhost:27017/'

#all ObjectID are generated in the same way, for the same reason
#each update overrides if it already exists, and adds it if it doesn't exist
#adds the item to the database
def updateSearchItem(item, text):
	client = MongoClient(localdb)
	botdb = client.botdb
	searchItems = botdb.searchItems

	#creating a unique ID using the names so that the command can be easily accessed
	#using hashing, extremely rare to have duplicate ID
	id = ObjectId(hashlib.md5(item.encode('utf-8')).hexdigest()[:24])
	searchItems.update({'_id': id},{'$set': {'text': text}}, upsert=True)
	client.close

#Adds location to database
def updateLocation(area, region, zone):
	client = MongoClient(localdb)
	botdb = client.botdb
	locations = botdb.locations

	id = ObjectId(hashlib.md5(area.encode('utf-8')).hexdigest()[:24])
	locations.update({'_id': id},{'$set': {'region': region,'zone': zone}}, upsert=True)
	client.close

#more optimization needed
#Adds region to database, since region is searched by using the region element, encoding not needed
def insertRegion(region, zone):
	client = MongoClient(localdb)
	botdb = client.botdb
	locations = botdb.locations

	locations.insert({'region': region,'zone': zone})
	client.close
	return zone

#returns the command if found
def obtainSearchItem(item):
	client = MongoClient(localdb)
	botdb = client.botdb
	searchItems = botdb.searchItems

	id = ObjectId(hashlib.md5(item.encode('utf-8')).hexdigest()[:24])
	item = searchItems.find_one({'_id': id})
	client.close
	if item == None:
		return None
	return item['text']

#returns location if found
def obtainLocation(area):
	client = MongoClient(localdb)
	botdb = client.botdb
	locations = botdb.locations

	id = ObjectId(hashlib.md5(area.encode('utf-8')).hexdigest()[:24])
	loc = locations.find_one({'_id': id})
	client.close
	if loc == None:
		return None
	return [loc['region'],loc['zone']]

#returns region if found
def obtainRegion(region):
	client = MongoClient(localdb)
	botdb = client.botdb
	locations = botdb.locations

	loc = locations.find_one({'region': region})
	client.close
	if loc == None:
		return None
	return loc['region']