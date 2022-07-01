#Write telephone directory of 10 students using dictionary and perform operation
#A) finding value-key:value
#B) replacing value-key: new value
#C) replacing key value - delete key and insert new key
def star():
    for i in range(0,60):
        print("*",end=' ')
    print('\n')

tel_dict={"Aarti":9112799815 ,"Tanvi":9112974690, "Sheetal":9326213813, "Gauri":8767507778,"Akanksha":8856919915, "Kirtee":7218685085, "Meena":7276215782,"Pavan":9145120629,"Pritam":9975398771,"Kalpana":9503724139}
print("Telephone directory is :")
print(tel_dict)
#A) finding value-key:value
key=str(input("Enter key to find value:"))
print("Telephone number of given key "+key +" is :")
for i in tel_dict.keys():
    if i==key:
        print(tel_dict[i])
        
star()      
#B) replacing value-key : new value
key=str(input("Enter key to find value:"))
value=str(input("Enter new value :"))
for i in tel_dict.keys():
    if i==key:
        tel_dict[i]=value
print("Telephone directory after replacement :")
print(tel_dict)

star()
#C)replacing key value -delete key and insert new key

num = int(input("Enter telephone number :"))
name =  str(input("Enter new key name :"))
old_key =0
for key,value in tel_dict.items():
    if num==value:
        old_key = key
tel_dict[name] = tel_dict.pop(old_key)

print("Dictionary after replacing key:value :")
print(tel_dict)    
