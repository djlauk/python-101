def add(a, b):
    return a + b

three = add(1, 2)

s1 = 'hello'

# lists hold multiple values. the value can have different types.
li1 = ['a', add(2, 3), 123.456, add]
print(li1[3](9, 1))
li1[3] = print  # lists are mutable; the contents can change after list creation
li1[3]('hoi zäme!')
li1.append(add)
li1.append(None)


# copy & paste from li1, swap [ ]  for ( )
# and you have a tuple.
#
# Main difference: lists are mutable, tuples are immutable (cannot be changed after creation)
t = ('a', add(2, 3), 123.456, add)
print(t[3](9, 1)) 
# t[3] = print  # not allowed. tuple is immutable
# t[3]('hoi zäme!')  # t[3] is still function 'add', so this doesn't make sense
# t.append(add)  # not allowed. tuple is immutable and has no ``append`` method
# t.append(None)  # not allowed. tuple is immutable and has no ``append`` method


# Dictionaries are data structures that are optimized for looking up
# values using a key. Think e.g. of a phone book:
# You know the name, and want to get to the phone number.
#
# Keys and values can have different types.
# Not every type can be used as a key though: The key needs to be "hashable".
d = {
    'alice': '555-1234',
    'bob': '555-2345',
    'claire': 5553456,
    '5553456': 'claire',
    '5552345': 'bob',
    '5551234': 'alice',
}
print(d['claire'])
