import random
count=0
for i in range(1,10):
    guessnum = int(input("Enter the guess number: "))
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    if guessnum==num1 or guessnum==num2:
        print("You get 1 point")
        count=count+1
    else:
        print("You didn't get any point")
print("Total point is:",count)


