# Hello world demo combining the bottle framework with the pymongo client.

import bottle
import pymongo

# This is the handler for the default path of the web server

# Decorator that executes the next function when user hits the '/' route.
@bottle.route('/')
def index():

  # connect to mongoDB
  connection = pymongo.MongoClient('localhost', 27017)

  # attach to test database
  db = connection.test

  # get handle for names collection
  name = db.names

  # find a single document
  item = name.find_one()

  # %s will be substituted by what is after the % sign.
  return '<b>Hello %s!</b>' % item['name']

# tell bottle to start running
bottle.run(host='localhost', port=8082)
