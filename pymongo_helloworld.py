# Hello world using pymongo with a local MongoDB server.
# Usage: python pymongoHelloWorld.py

import pymongo

from pymongo import MongoClient

# Connect to db
connection = MongoClient('localhost', 27017)

# Connect to test database
db = connection.test

# Handle to names collection
names = db.names

# Save name in collection
names.save({'name' : 'Mr. Hat'})

# Get first record from collection
item = names.find_one()

print 'Hello ' + item['name']

# Remove name from collection
names.remove({'name' : 'Mr. Hat'})
