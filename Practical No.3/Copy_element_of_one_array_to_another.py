#Copy all elements of one array into another

arr1=[2,5,8,6,1,4];
arr2=[None]*len(arr1);

for i in range(0,len(arr1)):
    arr2[i]=arr1[i];

print("Elements in original array:");
for i in range(0,len(arr1)):
    print(arr1[i]);
print();

print("Elements in new array:")
for i in range(0,len(arr2)):
    print(arr2[i]);
    
