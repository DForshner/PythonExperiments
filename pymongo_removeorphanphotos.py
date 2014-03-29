import sys
import pymongo

def getConnection():
  connection = pymongo.MongoClient("mongodb://localhost", safe=True)
  return connection.photos

def findOrphans(db):
  query = {}

  try:
    images = db.images.find(query)
  except:
    print "Unexpected error:", sys.exc_info()[0]

  for image in images:
    match = { 'images':image['_id']}
    print '\n Image: ', match 

    album = db.albums.find_one(match)

    if album == None:
      print '-------- ORPHAN: '
      db.images.remove({'_id':image['_id']})

    else:
      print '\n       Album: ', album['_id']

#  for doc in cursor:
#    print '\n', doc['name']
#    lowest = None
#    for score in doc['scores']:
#      print score
#      if (score['type'] == 'homework'):
#        if (lowest is None or score['score'] < lowest['score']):
#          lowest = score
    
#    print 'Removing lowest score: ', score

#    students.update({'_id':doc['_id']}, doc)
    
#    updatedStudent = students.find_one({'_id':doc['_id']})

#    for score in updatedStudent['scores']:
#      print score

db = getConnection()
orphans = findOrphans(db)
deleteOrphans(orphans)
