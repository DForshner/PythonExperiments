import json
import urllib2
import pymongo

def getStories(stories):
  print "\nLoading Reddit stories ---------------------------------" 

  # Read .json version of reddit home page
  home_page = urllib2.urlopen("http://reddit.com/.json")

  # Read page into json parser which converts json into python objects
  parsed = json.loads(home_page.read())


  # Iterate over the children of sub document 'data'
  for item in parsed['data']['children']:
    print "Title: " + str(item['data']['title'])
    stories.insert(item['data'])

def find(stories):
  print "\nStories with video ---------------------------------" 

  #Only returns documents that contains the sub doc .oembed.type
  query = {'media.oembed.type':'video'}
  projection = { 'media.oembed.url':1, '_id':0}

  try:
    cursor = stories.find(query, projection)
  except:
    print "Unexpected error: ", sys.exc_info()[0]

  for doc in cursor:
    # Returns doc in form {u'media': {u'oembed': {u'url': u'foo'}}}
    print doc

def getConnection():

  # Get db handle
  connection = pymongo.Connection("mongodb://localhost", safe=True)
  db=connection.reddit
  return db.stories

stories = getConnection()
getStories(stories)
find(stories)
