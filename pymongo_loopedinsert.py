import sys
import pymongo
import random

def createStudents():

  connection = pymongo.MongoClient("mongodb://localhost")
  db = connection.school
  scores = db.scores

  recordTypes = [ "exam", "homework", "quiz" ]

  for i in range (1, 101):
    for t in range (0, 2):
      score = random.uniform(0,100)
      student = { "student_id" : i, "record_type":recordTypes[t], "score":score}
      print "\nInsert"
      print student
      try:
        scores.insert(student)
      except:
        print "Insert failed: ", sys.exc_info()[0]

createStudents()
