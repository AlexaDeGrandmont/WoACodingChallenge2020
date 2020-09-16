'''
CCSS WoA Coding Challenge - Day 2 Medium (Project Euler #2 https://projecteuler.net/problem=2)

'''

fib = [0,1]
evenfibsum = 0
while fib[0] + fib[1] < 4000000000000:
    fib.append(fib[0] + fib[1])
    fib.pop(0)
    evenfibsum += fib[1] if fib[1] % 2 == 0 else 0

print(evenfibsum)

#Answer: 4613732