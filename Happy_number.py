#To check if given number is happy number

def HappyNumber(num):
    rem=sum=0;
    while(num>0):
        rem=num%10;
        sum=sum+ (rem*rem);
        num=num//10;
    return sum;

num=82;
result= num;

while(result !=1 and result !=4):
    result =HappyNumber(result);

if(result==1):
    print(str(num) + "is a Happy Number");
elif(result==4):
    print(str(num) + "is not a Happy Number");
