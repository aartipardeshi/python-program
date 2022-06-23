#Print largest and smallest element in array
#method 1
arr=[2,4,3,1,5,6,8,9];
mini=arr[0];
maxi=arr[0];

for i in range(len(arr)):
    if arr[i]>maxi:
        maxi=arr[i];
    if arr[i]<mini:
        mini=arr[i];
    

print("Largest element of array :" , maxi);
print("Smallest element of array :" , mini);

#method 2

arr=[2,4,3,1,5,6,8,9];
arr.sort()
print("Largest and smallest elements are :");
print(arr[-1])
print(arr[-0])

#method 3

arr=[2,4,3,1,5,6,8,9];
print("Largest and smallest elements are :");
print(max(arr));
print(min(arr));
