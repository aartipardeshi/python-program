#Program to check if a number is perfect number

num=int(input("Enter the number: "))  
sum1=0  
for i in range(1,num):  
    if (num%i==0):  
        sum1=sum1+i  
if(sum1 == num):  
    print("The entered number is a perfect number")  
else:  
    print("The entered number is not a perfect number")  
