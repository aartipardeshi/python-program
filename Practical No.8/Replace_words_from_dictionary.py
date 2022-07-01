#Python program to replace words from dictionary
dict={1:"aarti",3:"sheetal",5:"tanvi",4:"akanksha",2:"kirtee"}
key=int(input("Enter the key to replace value:"))
value=str(input("Enter new value:"))
for i in dict.keys():
    if(i==key):
        dict[i]=value
print("Dictionary after replacement:",dict)
