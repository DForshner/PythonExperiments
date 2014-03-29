# Examples of looping over list/dicts

print("\nLoop over list")

fruit = ['apple','orange','grape'] # init array

new_fruit = []

for item in fruit:  #iterate
  print item # Indent implies control flow

# append only executes once with the last value of item 
new_fruit.append(item)

print(new_fruit)


print("\nLoop over dictionary")

person = {'name':'Mr. Hat', 'favorite_color':'blue'}

for key in person: #iterate
  print "key is " + key + " value is " + person[key]


print("\nLoop over dictionary + list")

customer = { 'name':'Tim', 'favorite_color':'red',
'interests':['cycling','running','biking']}

for key in customer:

  # If the key is interests then loop over interests in the list
  if (key == 'interests'):
    print('Interests ....')
    for interest in customer[key]:
      print "\tinterests is " + interest

  else:
    print('Key is ' + key + ' value is ' + customer[key])

print("\nWhile loop over list")

fruit = ['apple', 'pear', 'orange']
i = 0
while(i < len(fruit)):
  print fruit[i]
  i = i + 1


print("\nHow many times does item appear in list")

fruit = ['apple', 'orange', 'grape', 'kiwi', 'orange', 'apple']

# Returns item frequency in list
def ItemFrequency(l):

  counts = {}
  for item in l:
    
    if item in counts:
      counts[item] = counts[item] + 1
    else:
      counts[item] = 1

  return counts

counts = ItemFrequency(fruit)

# prints out resulting dictionary
print counts
