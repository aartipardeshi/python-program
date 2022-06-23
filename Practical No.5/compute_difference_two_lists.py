#program to compute the difference between 2 list

def list_diff(list1, list2):
        out =[]
        for ele in list1:
                if not ele in list2:
                        out.append(ele)
        return out
list1=[11, 14, 20, 25, 10, 17]
print("First list is :", list1)
list2=[14,17,20, 15]
print("Second list is : " ,list2)

print(" The difference between first and second list :")
print(list_diff(list1,list2))
print(" The difference between second and first list :")
print(list_diff(list2,list1))

