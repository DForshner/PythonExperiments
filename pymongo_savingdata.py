import sys
import pymongo

def main():

  connection = pymongo.MongoClient("mongodb://localhost")
  db = connection.test
  people = db.people

  person = { 'name':'Tim Taylor', 'job':'Handy Man', 
      'address': { 'address1':'Some Address',
                    'street':'Some Street',
                    'state':'Some State',
                    'city':'Some City'},
      'interests':['fixing stuff', 'breaking stuff', 'cars']}

  print "\nFirst insert\n"
  print(person)
  try:
    people.insert(person)
  except:
    print "\nFirst insert failed: ", sys.exc_info()[0]

  # At this point person has been updated with an _id field which should cause the second
  # insert to fail.

  print "\nSecond Insert\n"
  print(person)
  try:
    people.insert(person)
  except:
    print "\nSecond insert failed: ", sys.exc_info()[0]

  # If we remove the id field the record can be inserted which will create two
  # records with different ids.
  del(person['_id'])

  print "\nThird Insert\n"
  print(person)
  try:
    people.insert(person)
  except:
    print "\nThird insert failed: ", sys.exc_info()[0]

  print "\nSaved records:\n"
  for record in people.find():
    print(record)
    people.remove(record)

main()
