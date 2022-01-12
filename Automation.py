import cv2
import time
import dropbox
import random

print("Calculator + Picture")
print("get your picture while running this program after every 2 minutes. Same time do your calculation!")
print(' 1 To Add')
print(' 2 To Subtract')
print(' 3 To Multiply')
print(' 4 To Divide')

choice =   int(input("Please select your type:- "))
num1   =   int(input("Enter The First Number:- "))
num2   =   int(input("Enter The Second Number:- "))

addNumber = num1 + num2
subNumber =num1 - num2
multiplyNumber = num1 * num2
divideNumber = num1 / num2

if choice == 1:
    print("Your Answer = ", addNumber)
elif choice == 2:
    print("Your Answer = ",subNumber)
elif choice == 3:
    print("Your Answer = ",multiplyNumber)
elif choice == 4:
    print("Your Answer = ",divideNumber)
else:
    print("The type you selected is invalid")    

main()