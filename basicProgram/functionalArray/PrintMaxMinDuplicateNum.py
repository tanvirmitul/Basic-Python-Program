#Generate 20 random numbers from 0 to 100 and print the max, min and duplicate random numbers (if any)

import random
import numpy as np
list=[]
for i in range(0,20):
    randomNum=random.randint(0,100)
    list.append(randomNum)

print(list)
max=list[0]
min=list[0]
print("Duplicate number is: ")
for i in range(0,len(list),1):
    if list[i]>max:
        max=list[i]
    if list[i]<max:
        min=list[i]
    for j in range(i+1,len(list),1):
        if list[i]==list[j]:
            print(list[i])

print("Max num is:",max)
print("Min num is:",min)