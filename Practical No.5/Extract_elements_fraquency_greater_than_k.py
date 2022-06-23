#Extract elements with frequency greater than k

list = ['a','b','c','b','d','a','c','b','a']
print("The original list : " + str(list))
K=2
print("K=2")

res = []
for i in list:
	freq = list.count(i)

	if freq > K and i not in res:
		res.append(i)
print("The repeated elements : " + str(res))
