import sys
import pymongo

# Gets a sequence of unique numbers from mongo.
# Mongo does not have transactions but it does have
# atomic operations on documents.

def get_collection():
  # Create connection to local mongo server 
  # safe=True causes driver to wait for response from server
  connection = pymongo.MongoClient("mongodb://localhost", safe=True)
  db = connection.test
  return db.counters


def get_next_sequence_numbers(counters, name):

  # find_and_modify can be used to find/insert a document,
  # modify it, and return the old or new value.

  counter = counters.find_and_modify(
      query={'type':name}, # user_id, sequence_number, etc.
      update={'$inc':{'value':1}}, # increment value by one.
      upsert=True, # if there isn't a doc of type name create one.
      new=True # Return the new value of the doc instead of the old value.
      )

  counter_value = counter['value']

  return counter_value;


counters = get_collection()

print "\nNext three sequence numbers for uid1:"
print get_next_sequence_numbers(counters, 'uid1')
print get_next_sequence_numbers(counters, 'uid1')
print get_next_sequence_numbers(counters, 'uid1')

print "\nNext sequence numbers for user_uid:"
print get_next_sequence_numbers(counters, 'user_uid')

print "\nRecords:"
for doc in counters.find():
  print doc
