#1 Empty list
my_list=[]

print(my_list)

#2 Append Elements
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

print(my_list)

#3 Insert Element
my_list.insert(1, 15)

print(my_list)

#4 Extend List
my_list.extend([50, 60, 70])
print('Extended List:', my_list)

#Remove Element
my_list.pop()

#Sort List
my_list.sort()

print(my_list)

#Find Item
index_30=my_list.index(30)
print('Index of 30:', index_30)