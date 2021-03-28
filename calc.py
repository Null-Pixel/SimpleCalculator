import os

def op():
    op = int(input("Enter op: 1 +, 2 -, 3 *, 4 /, kill-process 0: "))

    ans = None
    if op == 1:
        num1 = int(input("Enter 1. num: "))
        num2 = int(input("Enter 2. num: "))
        ans = num1 + num2
        print (ans)

    if op == 2:
        num1 = int(input("Enter 1. num: "))
        num2 = int(input("Enter 2. num: "))
        ans = num1 - num2
        print (ans)

    if op == 3:
        num1 = int(input("Enter 1. num: "))
        num2 = int(input("Enter 2. num: "))
        ans = num1 * num2
        print (ans)

    if op == 4:
        num1 = int(input("Enter 1. num: "))
        num2 = int(input("Enter 2. num: "))
        ans = num1 / num2
        print (ans)
        
    if op == 0:
        exit()

for i in range(100):
    op()
    