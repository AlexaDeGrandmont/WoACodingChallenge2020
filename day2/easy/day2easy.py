'''
CCSS WoA Coding Challenge - Day 2 Easy (Project Euler #20 https://projecteuler.net/problem=20)

'''

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

def split(word):
    return [char for char in word]

fact = factorial(100)

factList = split(str(fact))

numSum = 0

for num in factList:
    numSum += int(num)

print(numSum)

#Answer: 648