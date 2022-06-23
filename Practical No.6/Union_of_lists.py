#Program to find union of two lists

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

ans=[]
for i in list1:
    if i not in ans:
        ans.append(i)
for i in list2:
    if i not in list1:
        ans.append(i)

print("The union of two list : ",ans)
