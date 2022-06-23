# To check if the list contain 3 consecutive common numbers

list= [ 3, 3, 3, 5, 12, 13, 7]
print("Input list is :", list)
size = len(list)

for i in range(size - 2):
        if list[i] == list[i + 1] and list[i + 1] == list[i + 2]:
                print("The 3 consecutive common number in list : ",list[i])
