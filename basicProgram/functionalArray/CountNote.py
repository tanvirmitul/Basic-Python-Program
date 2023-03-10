# Input an amount from the user and find out the number of notes from input amount in given array
# [1000,500,100,50,20,10,5,2,1]
# Input: 1256
# Output:
# 1000 1
# 100 2
# 50 1
# 5 1
# 1 1
list=[1000,500,100,50,20,10,5,2,1]
amount=int(input("Enter amount: "))
for i in list:
    print(i,amount//i)
    amount=amount%i