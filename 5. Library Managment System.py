"""This program is desgined to manage a library 
   like adding a book make list books already added"""

print("WELCOME TO LIBRARY MANAGEMENT SYSTEM")

class library:
    no_of_books = 0
    Books = []

    def lib_manage():
        ope = int(input("0 to add a book , 1 to end the management : "))
        if(ope==0):
            book = input("Enter the name of book : ")
            library.Books.append(book)
            library.no_of_books += 1
            library.lib_manage()
        elif(ope==1):
            return
        else:
            raise ValueError("invalid value entered")


library.lib_manage()

print(f"\n\nThere are {library.no_of_books} books in library")
print(f"Books in library : {library.Books}")