sum=0
ch='a'
while ch!='q':
    num=int(input("Enter your number: "))
    sum=sum+num
    print("Enter c for continue & q for quit")
    ch=input("Enter your choice: ")[0]
    if ch=='q':
        break
    if ch=='c':
        continue
print("Sum of user input is:",sum)