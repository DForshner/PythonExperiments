import sys
import pymongo
import random

def getConnection():
  # Create connection to local mongo server 
  # safe=True causes driver to wait for response from server
  connection = pymongo.MongoClient("mongodb://localhost", safe=True)
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

def findLastTenDocsSortedByStudentID(scores):
  print "\nFinding last 10 records sorted by student id.\n"
  query = {}
  projection = { 'student_id':1, '_id':0}

  try:
    # The order of operations is always sort -> skip -> limit in the db 
    # so the cursor can be configured in any order.
    cursor = scores.find(query,projection).sort('student_id', pymongo.DESCENDING)

    # The sort operation uses a tuple because if a dictionary was used the order
    # would not be retained.  Multiple keys are passed in an array.
    # Ex: .sort([('student_id',pymongo.ASCENDING),('score',pymongo.DESCENDING)])

    # Can also define each operation on seperate lines
    cursor = cursor.limit(10);

  except:
    print "Unexpected error:", sys.exc_info()[0]

  # The query is not run until we start to iterate over the cursor.
  for doc in cursor:
    print doc


scores = getConnection()
scores.remove()

createStudents(scores)
findStudents31To40(scores)
findOneStudent(scores)
findExamScoresBetween(scores, 99, 100)
findLastTenDocsSortedByStudentID(scores)
