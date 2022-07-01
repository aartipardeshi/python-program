#Take two list as input and convert them into dictionary and print dictionary

print(" Elements of first list is : ")
list1= list(map(str,input().split()))
print("Elements of second list is :")
list2= list(map(str,input().split()))

#dictionary=dict(zip(list1,list2))

dictionary={}
for key in list1:
    for value in list2:
        dictionary[key] = value
        list2.remove(value)
        break
print("Dictionary is : ", str(dictionary))
