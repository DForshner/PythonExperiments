"""
Tutorial code on using args and kwargs in python.

Usage: python argskwargs_demo.py 
"""

print '\n\n*args allows you pass an arbitrary number of arguments to your function.'
def print_everything(*args):
	for count, thing in enumerate(args):
		print '{0}. {1}'.format(count, thing)

print_everything('apple', 'banana', 'cabbage')

print '\n\n**kwargs allows you to handle named arguments that you have not defined in advance.'
def table_things(**kwargs):
	for name, value in kwargs.items():
		print '{0} = {1}'.format(name, value)

table_things(apple = 'fruit', cabbage = 'vegetable')

print '\n\nExplicit arguments get values first and then everything else is passed to *args and *kwargs.'
def title_table_things(titlestring, **kwargs):
	print 'Title: {0}'.format(titlestring)
	for name, value in kwargs.items():
		print '{0} = {1}'.format(name, value)

title_table_things('Cool table bro!', apple = 'fruit', cabbage = 'vegetable')

print '\n\nUsing the * syntax takes the list (or tuple) of items and matches them to the arguments in the function.'
def print_three_things(a, b, c):
	print 'a = {0}, b = {1}, c = {2}'.format(a,b,c)

mylist = ['aardvark', 'baboon', 'cat']
print_three_things(*mylist)
