a=int(input("Enter the number:"))
b=int(input("Enter the 2nd number:"))
c=int(input("Enter the 3rd number:"))
if a>b and a>c:
    print("greater number is:",a)
elif b>a and b>c:
    print("greater number is:",b)
else:
    print("greater number is:",c)