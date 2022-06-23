#Program to count the occurrence of each word in a given sentence

string=str(input("Enter the sentence :"))
arr=[]
arr=string.split()
i=0
count=0
print("Given sentence is :", string)
print("occurence of each word :")
while(i<len(arr)):
    count=0
    for j in arr:
        if arr[i]==j:
            count=count+1
    print(arr[i],"occures", count, "times")
    i=i+1
