#Program to find count tuple occurrance in list of tuple

import collections 
result = collections.defaultdict(int)
tuple = [[('A','B','C')],[('P','O','R')],[('M','N','S')]]

for elem in tuple:
      result[elem[0]] += 1
print("Count of tuples present in list of tuple is :\n ",result)
