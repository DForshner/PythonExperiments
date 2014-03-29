import sys
import pymongo

def getConnection():
  connection = pymongo.MongoClient("mongodb://localhost", safe=True)
  db = connection.school
  return db.students

def findStudents(students):
  query = {}

  try:
    cursor = students.find(query)
  except:
    print "Unexpected error:", sys.exc_info()[0]

  for doc in cursor:
    print '\n', doc['name']
    lowest = None
    for score in doc['scores']:
      print score
      if (score['type'] == 'homework'):
        if (lowest is None or score['score'] < lowest['score']):
          lowest = score
    
    print 'Removing lowest score: ', score
    doc['scores'].remove(lowest)

    students.update({'_id':doc['_id']}, doc)
    
    updatedStudent = students.find_one({'_id':doc['_id']})

    for score in updatedStudent['scores']:
      print score

students = getConnection()
findStudents(students)
