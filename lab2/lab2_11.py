# Accessing elements in a set
my_set = {1, 2, 3, 4, 5}
print(3 in my_set)

# Adding elements to a set
my_set.add(6)
print(my_set)

# Removing elements from a set
my_set.remove(2)
print(my_set)

# Looping through a set
for item in my_set:
    print(item)

# Joining two sets
another_set = {7, 8, 9}
joined_set = my_set.union(another_set)
print(joined_set)

# Set methods
print(my_set.intersection(another_set))
print(my_set.difference(another_set))
print(my_set.symmetric_difference(another_set))