# Take input from a user and check if the number exists in the array
# let the array is [1,3,5,7,2,4,6,8]
# Input: 7
# Output: Found in the position 3
# Input: 9
# Output: Found no element

list=[1,3,5,7,2,4,6,8]
num=int(input("Enter num: "))
i=0
count=0
while i<len(list):
    if num==list[i]:
        print("Number found at position",i)
    else:
        count=count+1
    i=i+1
if count==len(list):
    print("No element found")

