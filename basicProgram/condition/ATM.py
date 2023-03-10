#Write a program to check balance and withdraw money from ATM booth using if else or switch case

print("Welcome to the booth")
print("Please choose any option")
print("1. Check balance")
print("2. Withdraw balance")
print("3. Deposit balance")
print( "4. Exit")

opt=int(input("Enter your option: "))
amount=12500.00; new_amount=0.00

if opt==1:
    print("Your current balance is:",amount)
elif opt==2:
    withdrawAmount=float(input("Enter your withdraw amount: "))
    if amount>=withdrawAmount:
        currentBalance=amount-withdrawAmount
        print("Your withdraw amount is:",withdrawAmount)
        print("Your current balance is:",currentBalance)
    if amount<withdrawAmount:
        print("You don't have sufficient balance")
elif opt==3:
    depositbalance=float(input("Enter your deposit balance: "))
    newAmount=amount+depositbalance
    print("Your current balance is",newAmount)
elif opt==4:
    print("Thank you using our service")
else:
    print("You've entered wrong input, Please enter correct input")