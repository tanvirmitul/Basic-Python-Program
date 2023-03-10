# Write a program to check if inputted letter is small or capital
char=input("Enter character: ")[0]
if char.isupper():
    print(char,"is upper case")
elif char.islower():
    print(char,"is lowercase")
else:
    print(char,"is not alphabet")