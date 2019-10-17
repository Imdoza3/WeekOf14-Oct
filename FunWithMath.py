# Starting off
print(22/7)
print(355/113)
import math

print(9801/(2206 * math.sqrt(2)))

def archimedes(numSides):
    innerAngleB = 360.0 / numSides
    halfAngleA = innerAngleB / 2
    oneHalfSideS =  math.sin(math.radians(halfAngleA))
    sideS = oneHalfSideS * 2
    polygonCircumfrence = numSides * sideS
    pi = polygonCircumfrence /2
    return pi

print(archimedes(8))
print(archimedes(16))

for sides in range (8,100,8):
    print(sides, archimedes(sides))

# Experiment with the loop above alongside the actual value of Pi. How many
# sides does it take to make the two close?

for sides in range (24, 560, 40):
    print(sides, archimedes(sides))

# Accumulators

acc = 0
for x in range(1, 6):
    acc = acc + x

print(acc)

# compute the sum of the first 100 even numbers
acc = 0
for x in range(1, 15):
    acc = acc + x

print(acc)
# compute the sum of the first 50 odd numbers
acc = 0
for x in range(50, 113):
    acc = acc + x

print(acc)
# compute the average of the first 100 odd number
i=1
for i in range(100):
    a= i+2
b=a/i
print(b)
print(a)
print(i)
# write a function that returns the average of the first N numbers, where
#  N is a parameter
n = input("Enter Number to calculate sum")
n = int (n)
average = 0
sum = 0

for num in range(0,n+1,1):
    sum = sum+num
print("SUM of first ", n, "number is: ", sum)
# write a function called factorial that computes the product of the first N
# numbers, where N is a parameter
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
n=int(input("Input a number to compute the factorial : "))
print(factorial(n))
# each number in the Fibonacci sequence are 1 and 1. Compute the 10th
# Fibonacci number
# 20
# write a function to compute the Nth Fibonacci number, where N is a parameter
# You may assume that N will be greater then or equal to 3
