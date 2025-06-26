#Program for calculate Factorial using recursion function.

inNum = int(input("Enter a number for calculate Factorial : "))

def factorial(inNum):
    if inNum < 2 :
        return 1
    else :
        return  inNum * (factorial(inNum -1))

result = factorial(inNum)
print("Factorial of ", inNum, "is :",result)