#Library operation
#1)Issue
#2)Return
def star():
    for i in range(0, 40):
        print("*", end=' ')
    print('\n')
    
books={1760:'Alibaba ani 40 chor', 1250:'Cinderlla', 1530:'Moon lights', 2390:'Arabian Nights',1280:'Harry Potter'}
Issued_book={}
#1)Issue a book
key=int(input("Enter book id to issue :"))
issue_b=books.pop(key)
Issued_book[key]=issue_b
print("Book which is issued :")
print(Issued_book)
print("After Issuing of book  of id "+ str(key)+" dictionary is :")
print(books)

star()
#2)Returning a book
print("After Returning of book  of id "+ str(key)+" dictionary is :")

books.update(Issued_book)
print(books)
