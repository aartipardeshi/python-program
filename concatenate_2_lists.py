#Program to concatenate 2 list

list1 = ['a', 'b', 'c']
list2 = [1, 2, 3, 4]
print("list1=", list1)
print("list2=",list2)

list3=[x+str(y) for x in list1 for y in list2]
print("list after concatenation :" , list3)
