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


# A Monte Carlo Simulation

import random

print(random.random())

# Bolean expressions
# > greater than
# >= greater than or equal to
# < less than
# <= less than or equal to
# == the same as [equal to ]
# != NOT equal to

dogWeight = 25
print(dogWeight != 25)
catWeight = 15

# compound Boolean operators
# and
# or
# not
print(not catWeight < 20)



def montePi(numDarts):

    inCircle = 0

    for i in range(numDarts):
        x = random.random()
        y = random.random()

        distance = math.sqrt(x**2 + y**2)

        if distance <= 1:
            inCircle = inCircle + 1

    pi = inCircle / numDarts *4
    return pi

print(montePi(100))

import turtle

def showMontePi(numDarts):
    scn = turtle.Screen()
    t = turtle.Turtle()

    scn.setworldcoordinates(-2,-2,2,2)

    t.penup()
    t.goto(-1,0)
    t.pd()
    t.goto(1,0)

    t.pu()
    t.goto(0,1)
    t.pd()
    t.goto(0,-1)

    inCircle = 0
    t.pu()

    for i in range(numDarts):
        x = random.random()
        y = random.random()

        distance = math.sqrt(x**2 + y**2)

        t.goto(x,y)
