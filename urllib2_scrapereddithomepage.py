import json
import urllib2

# Gets a list of stories from the reddit homepage

# Read .json version of reddit home page
home_page = urllib2.urlopen("http://reddit.com/.json")

# Read page into json parser which converts json into python objects
parsed = json.loads(home_page.read())

print "\n\n Reddit Front Page Stories ---------------------------------" 

# Iterate over the children of sub document 'data'
for item in parsed['data']['children']:
  print "\nTitle: " + str(item['data']['title'])
  print "Permalink:" + str(item['data']['permalink'])
