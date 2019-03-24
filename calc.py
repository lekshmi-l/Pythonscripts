a=input("Enter the first number ")
b=input("Enter the second number ")
i=input("Enter the operator ")
def add(a,b):
    c=int(a)+int(b)
    print("Sum of the given number is", c)
    return c
def sub(a,b):
    d=int(a)-int(b)
    print("Difference of the given number is", d)
    return d
def mul(a,b):
    e=int(a)*int(b)
    print("Product of the given number is", e)
    return e
def divd(a,b):
    f=float(a)/float(b)
    print("Division of the given number is", f)
    return f
def noparameter(i):
    return(print("Invalid operator selected :" ,i))

    

if(str(i)=='+'):
    add(a,b)

elif(str(i)=='-'):
    sub(a,b)

elif(str(i)=='*'):
    mul(a,b)

elif(str(i)=='/'):
    divd(a,b)

else:
    noparameter(i)


    

