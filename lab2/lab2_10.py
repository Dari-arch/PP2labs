# Accessing elements in a tuple
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[0])
print(my_tuple[-1])

# Updating a tuple (tuples are immutable, so we need to create a new one)
my_tuple = (1, 2, 3, 4, 5)
new_tuple = my_tuple + (6,)
print( new_tuple)

# Unpacking a tuple
a, b, c, d, e = my_tuple
print(a, b, c, d, e)

# Looping through a tuple
for item in my_tuple:
    print( item)

# Joining tuples
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
joined_tuple = tuple1 + tuple2
print( joined_tuple)

# Methods for tuple
print(len(my_tuple))
print(my_tuple.count(2))
print( my_tuple.index(3))