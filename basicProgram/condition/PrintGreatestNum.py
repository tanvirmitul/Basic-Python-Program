num1=int(input("Enter first num: "))
num2=int(input("Enter second num: "))
num3=int(input("Enter third num: "))

if num1>num2 and num1>num3:
    print(num1,"is greatest number")
elif num2>num1 and num2>num3:
    print(num2,"is greatest num")
else:
    print(num3,"is greatest number")