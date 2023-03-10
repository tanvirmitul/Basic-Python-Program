#Take 5 numbers from users in an array. Then find out the average number,
# how many even and how many odd numbers using these functions: average(), countEvenNumbers(), countOddNumbers()

def countEven(arr):
    even = 0
    for i in arr:
        if i%2==0:
            even=even+1
    return even

def countOdd(arr):
    odd=0
    for i in arr:
        if i%2!=0:
            odd=odd+1
    return odd
def avg(arr):
    sum=0
    for i in arr:
        sum=sum+i
    avg=sum//len(arr)
    return avg

list=[]
print("Enter the elements: ")
for i in range(0,5):
    list.append(int(input()))

evenNum=countEven(list)
oddNum=countOdd(list)
avgNum=avg(list)
print("Total even num:",evenNum)
print("Total odd num:",oddNum)
print("Total avg",avgNum)
