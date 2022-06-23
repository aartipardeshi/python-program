
#Program to solve quadratic equation

import cmath

a=3
b=4
c=5
d=(b**2)-4*a*c

x=-b+cmath.sqrt(d)/2*a
y=-b-cmath.sqrt(d)/2*a

print("The solutions of quadratic equations are :")
print(x)
print(y)
