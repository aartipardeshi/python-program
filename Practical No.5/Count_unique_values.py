#Count unique values inside the list

list = [1, 2, 3,5,1,2,6,7]
print("Input list : ", list)
l1 = []
count = 0

for i in list:
	if i not in l1:
		count += 1
		l1.append(i)
print("Output list : ", l1)
print("No of unique elements are:", count)
