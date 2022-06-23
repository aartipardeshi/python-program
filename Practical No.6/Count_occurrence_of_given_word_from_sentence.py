#Program to count occurrence of given word in a given sentence

string=str(input("Enter the sentence :"))
word=str(input("Enter a word to find occurence:"))
arr=[]
count=0
arr=string.split(" ")
for i in range(0,len(arr)):
    if(word==arr[i]):
        count=count+1
print("Count of the word is :",count)
