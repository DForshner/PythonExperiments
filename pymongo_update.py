import sys
import pymongo
import random
import datetime

def get_collection():
  # Create connection to local mongo server 
  # safe=True causes driver to wait for response from server
  connection = pymongo.MongoClient("mongodb://localhost", safe=True)
  db = connection.school
  return db.scores

def create_students(scores):
  print "\nCreating student data."
  recordTypes = [ "exam", "homework", "quiz" ]

  for i in range (1, 101):
    for t in range (0, 2):
      score = random.uniform(0,100)
      student = { 'student_id' : i, 'record_type':recordTypes[t], 'score':score}
      try:
        scores.insert(student)
      except:
        print "Insert failed: ", sys.exc_info()[0]


def update_using_save(scores):
  print "\nWholesale update to add review to student 1."
  query = { 'student_id':1, 'record_type':'homework' }

  try:
    # Get doc
    score = scores.find_one(query)
    print "\nbefore: ", score

    # Add are ISO review date 
    score['review_date'] = datetime.datetime.utcnow()

    # wholesale update the record using convenience method
    # Note: if _id exists it's treated as update if not it's treated as insert
    scores.save(score)

    score = scores.find_one(query)
    print "\nafter: ", score

  except:
    print "Unexpected error:", sys.exc_info()[0]
    raise

def wholesale_update(scores):
  print "\nSelective update to add review field to student 2."
  query = { 'student_id':2, 'record_type':'homework' }

  try:
    # Get doc
    score = scores.find_one(query)
    print "\nbefore: ", score

    # Add are ISO review date 
    score['review_date'] = datetime.datetime.utcnow()

    # Selective update
    # If _id is different an exception would be thrown
    scores.update({'student_id':2, 'record_type':'homework'}, score)

    score = scores.find_one(query)
    print "\nafter: ", score

  except:
    print "Unexpected error:", sys.exc_info()[0]
    raise

def selective_update_using_set(scores):
  print "\nSelective update to add review field to student 3."
  query = { 'student_id':3, 'record_type':'homework' }

  try:
    # Get doc
    score = scores.find_one(query)
    print "\nbefore: ", score

    # Selective update using set
    # This is more efficient because only the review_date field is changed
    # instead of writing the entire document in the db.
    scores.update({'student_id':3, 'record_type':'homework'},
        {'$set':{'review_date':datetime.datetime.utcnow()}})

    score = scores.find_one(query)
    print "\nafter: ", score

  except:
    print "Unexpected error:", sys.exc_info()[0]
    raise

def selective_update_using_unset(scores):
  print "\nRemoving review date from all students."
  query = {'student_id':{'$lte': 3}, 'record_type':'homework' }

  try:
    # Multi-update to remove from all records in collection
    scores.update({}, {'$unset':{'review_date':1}},multi=True)
    cursor = scores.find(query).sort('student_id',pymongo.ASCENDING).limit(3)

  except:
    print "Unexpected error:", sys.exc_info()[0]
    raise

  for doc in cursor:
    print doc


def upserting(scores):
  print "\nUpserting student records."

  try:
    scores.drop()

    # Creates a student without a student_id because upsert normally
    # only uses the criteria on the right.
    scores.update({'student_id':1}, {'score':50}, upsert=True)

    # However the set comment causes both the left and right critria
    # to be used so this will create a student with both a student id and score
    scores.update({'student_id':2}, {'$set':{'score':100}}, upsert=True)

    cursor = scores.find().limit(100)

  except:
    print "Unexpected error:", sys.exc_info()[0]
    raise

  for doc in cursor:
    print doc


scores = get_collection()

# Clear any pre-existing data
scores.drop()

create_students(scores)
update_using_save(scores)
wholesale_update(scores)
selective_update_using_set(scores)
selective_update_using_unset(scores)
upserting(scores)
