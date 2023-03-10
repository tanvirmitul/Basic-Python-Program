num=int(input("Enter the num: "))
rem=0
while num!=0:
    rem=num%10
    print(rem)
    num=num//10

# num = int(input("Enter num: "))
# reversed_num = 0
#
# while num != 0:
#     digit = num % 10
#     reversed_num = reversed_num * 10 + digit
#     num //= 10
#
# print("Reversed Number: " + str(reversed_num))