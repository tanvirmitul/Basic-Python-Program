# Suppose a software system excepts valid credentials from user to logged in to the system.
# if the user inputs wrong password for 3 times,
# system will say that "Your user has been temporary locked". Let the username: admin, password: admin@123

username="admin"
password="admin@123"

i=0
count=0
enterUsername = input("Enter your username: ")
while i>=0:
    enterPassword=input("Enter your password: ")
    if enterUsername==username and enterPassword==password:
        print("Welcome to the system")
        break
    elif enterPassword!=password:
        count = count+1
        if count==1:
            print("You've entered wrong password, Please enter correct passowrd")
        if count==2:
            print("You've entered wrong password 2 times, if you again entered wrong password for 3rd times. You account will be blocked for 24 hours")
        if count==3:
            print("You've entered wrong password for 3rd. Now your account is blocked for 24 hours")
            break
    i=i+1

print("Thank you for using our system")



