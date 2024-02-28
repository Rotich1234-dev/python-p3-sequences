s = [4, 6, 3, 9, 3, 5, 1, 2]
# print (1 in s)
# print (s + s)
# print (s[2:5:2])
s.sort()
print(s)
sorted_list = sorted (s)
print(s)
print(sorted_list)

# modify list
my_list = [0, 1, 2, 3]
my_list[0] = None
print(my_list)

# adding items to list
my_list = [0, 1, 2, 3]
my_list.append(4)
print(my_list)
# => [0, 1, 2, 3, 4]

#list.insert() provides us a few extra options for 
# 

my_list = ['a', 'b', 'c', 'd', 'f']
my_list.insert(4, 'e')
print(my_list)
# => ['a', 'b', 'c', 'd', 'e', 'f']
my_list.insert(1000, 'g')
print(my_list)
# => ['a', 'b', 'c', 'd', 'e', 'f', 'g']


# list.pop() removes and returns the element at the index passed in as an argument. When used without any arguments, it removes and returns the last element of the list.

# list.remove() removes the element passed in as an argument. This is one of the few list methods that searches by value instead of index!

# 
# del() removes elements from a list, specified by an index or range of indices.
print (s.pop())
print (s.clear())

