print ("Hello")
print ("Hello", "World")

# The format operator (%) will substitute the collection
# values into the string.
print ("I have %d friggen %s." % (10, "cats"))
print ("Each cat eats %.2f mice per year on average." % 3.555)  # Displays 3.56

sqlist = [x*x for x in range(1, 10) if x % 2 != 0]
print sqlist
print [ch.upper() for ch in 'comprehension' if ch not in 'aeiou']
