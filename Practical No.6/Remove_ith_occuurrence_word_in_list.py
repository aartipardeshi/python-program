#Program to remove the ith occurrence of given word in a list where words repeat

list=[]
n=int(input("Enter the number of elements of list:"))
print("Enter elements of list :") 
for i in range(0,n):
    element=input()
    list.append(element)

print(" The given list is :",list)
li=[]
count=0
b=input("Enter word to remove =")
s=int(input("Enter the occurrence to remove :"))
for i in list:
    if(i==b):
        count=count+1
        if(count!=s):
            li.append(i)
    else:
         li.append(i)
if (count==0):
    print("Item not found")
else:
    print("The number of repetitions of word is :",count)
    print("Updated list is :",li)
    

