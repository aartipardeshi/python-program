#Program to find intersection of two list

n=int(input("Enter  number of elements of list1 :"))
list1=[]
print("Enter the elements of list1 :")
for i in range(0,n):
    ele=input()
    list1.append(ele)
    
m=int(input("Enter  number of elements of list2 :"))
list2=[]
print("Enter the elements of list2 :")
for i in range(0,m):
    ele=input()
    list2.append(ele)

print("First list is :",list1)
print("second list is :", list2)
val=[]
ans=[]
for i in list1:
    if i not in ans:
        ans.append(i)
for i in ans:
    if i in list2:
        val.append(i)

print("The intersection of two list : ",val)

