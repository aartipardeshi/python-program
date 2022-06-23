#Program to find the length of list using recursion

len=0
def length(list):
    global len
    if list :
        len=len+1
        length(list[1: ])
    return len
list=[5,7,6,3,4,8,9,2]
print("The list is : ", list)

len=length(list)
print(" The length of a list is : ",len)
