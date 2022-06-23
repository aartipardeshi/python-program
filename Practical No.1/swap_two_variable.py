
#Program to swap two variables

a=5
b=3

#method 1
a=a+b
b=a-b
a=a-b

print(a)
print(b)

#method 2
a,b=b,a
print(a)
print(b)

#method 3
x=7
y=4

temp=x
x=y
y=temp

print(x)
print(y)
