# Hello world demo for bottle framework
# Test by browsing url localhost:8080/hello/YourName

import bottle

# Import route, run, and template from bottle framework.
from bottle import route, run, template

# Create get request handler for route ../
@route('/')
def home_page():
  return "<!DOCTYPE html><html><title></title><body>Visit localhost:8080/hello/{Your name} for a custom greeting.\n</body></html>"

# Create get request handler for route ../hello/
@route('/hello/:name')
def index(name='World'):
  things = ['apple','orange','banana','peach']

  #Return HTML document using name given in the route.
  return template('BottleHelloWorld', {'name':name, 'things':things})

  # Could also have passed the parameters directly
  # Ex: return template('BottleHelloWorld', name = name, things = things)

# Create post request handler for route ../favorite_fruit/
@bottle.post('/favorite_fruit')
def favorite_fruit():
  fruit = bottle.request.forms.get("fruit")
  if (fruit == None or fruit == ""):
    fruit = "No fruit selected"

  bottle.response.set_cookie("fruit", fruit)

  # Send http response to browser to fetch new route using GET request.
  bottle.redirect("/show_fruit")

  # We could display HTML from post but the user cannot refetch a page that was
  # generated as a response from a POST request without reprocessing the form
  # information.
  # EX: return bottle.template('<!DOCTYPE html><html><title>Fruit Selection Confirmation</title><body>Your favorite fruit is: {{fruit}}</body></html>', {'fruit':fruit})

@route('/show_fruit')
def show_fruit():
  # gets fruit value from cookie
  fruit = bottle.request.get_cookie("fruit")
  
  return bottle.template('<!DOCTYPE html><html><title>Fruit Selection Confirmation</title><body>Your favorite fruit is: {{fruit}}</body></html>', {'fruit':fruit})

# Enable debugging
bottle.debug(True)

# Start listening on port 8080
run(host='localhost',port=8080)
