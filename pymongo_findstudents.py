import sys
import pymongo
import random

def getConnection():
  # Create connection to local mongo server 
  connection = pymongo.MongoClient("mongodb://localhost")
  db = connection.school
  return db.scores

def createStudents(scores):
  print "\nCreating student data.\n"
  recordTypes = [ "exam", "homework", "quiz" ]

  for i in range (1, 101):
    for t in range (0, 2):
      score = random.uniform(0,100)
      student = { 'student_id' : i, 'record_type':recordTypes[t], 'score':score}
      try:
        scores.insert(student)
      except:
        print "Insert failed: ", sys.exc_info()[0]


def findStudents31To40(scores):
  print "\nFinding exams for students 31 to 40.\n"
  query = { 'record_type':'exam' }

  # Projection the student id and surpress the _id field
  projection = {'student_id':1, '_id':0} 

  try:
    # get a cursor of documents we can iterate over.
    cursor = scores.find(query,projection).limit(10).skip(30)
  except:
    print "Unexpected error:", sys.exc_info()[0]

  for doc in cursor:
    print doc


def findOneStudent(scores):
  print "\nFinding a single document.\n"
  query = { 'student_id':10}

  try:
    doc = scores.find_one(query)
  except:
    print "Unexpected error:", sys.exc_info()[0]

  print doc


def findExamScoresBetween(scores, low, high):
  print "\nFinding exams with scores btween " + str(low) + " and " + str(high) + "\n"
  query = { 'record_type':'exam', 'score':{'$gt':low, '$lt':high} }
  projection = { 'student_id':1, 'score':1, '_id':0} 

  try:
    cursor = scores.find(query,projection)
  except:
    print "Unexpected error:", sys.exc_info()[0]

  for doc in cursor:
    print doc

def findLastTenStudentIDs(scores):
  print "\nFinding last 10 student id numbers."
  query = {}

  try:
    cursor = scores.find(query).sort('student_id', pymongo.ASCENDING).limit(10);
  except:
    print "Unexpected error:", sys.exc_info()[0]

  for doc in cursor:
    print doc


scores = getConnection()

createStudents(scores)
findStudents31To40(scores)
findOneStudent(scores)
findExamScoresBetween(scores, 99, 100)
findLastTenStudentIDs(scores)
