# create empty set
my_list = []

# append
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# insert 15 at the second place
my_list.insert(1, 15)

# extend
my_list.extend([50, 60, 70])

# remove the last element
my_list.pop()

# sort
my_list.sort()

print(my_list)

# Find and print index of value 30
index = my_list.index(30)
print("Index of 30:", index)