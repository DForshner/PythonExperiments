#!/usr/bin/env python

import sys
import json
import urllib
from subprocess import call
from urllib import urlopen
import os
import math

# Get the username from command line args
if len(sys.argv) != 2:
  print "\nUsername Required.  Example: python DisplayGitHubGists.py DForshner";
  sys.exit() 

user = str(sys.argv[1])
print ("\nGetting gists for: " + user)

# Get total number of gists
userurl = urlopen('https://api.github.com/users/' + user)
public_gists = json.load(userurl)
gistcount = public_gists['public_gists']

print ("Getting " + str(gistcount) + " gists\n")

# Get total number of gists pages
perpage=30.0
pages = int(math.ceil(float(gistcount)/perpage))

# Get gists from each page
for page in range(pages):
    u = urlopen('https://api.github.com/users/' + user + '/gists?page=' + str(page) + '&per_page=' + str(int(perpage)))
    gists = json.load(u)
    startd = os.getcwd()

    # Display info about each gist
    for gist in gists:
      gistid = gist['id']
      gistdesc = gist['description']
      print (gistid + " - " + gistdesc)
