# This is a basic calculator for add , sub. , product , division.

print("WELCOME TO BASIC CALCULATOR")

ope = input("enter the operation you wanna do\nadd , sub ,product , divide:")
a = int(input("enter first value:"))
b = int(input("enter second value:"))
if(ope == "add"):
    print("your result is:",a+b)
elif(ope == "sub"):
    print("your result is:",a-b)
elif(ope == "product"):
    print("your result is:",a*b)
elif(ope == "divide"):
    print("your result is:",a/b)
else:
    print("invailid operation")