'''
CCSS WoA Coding Challenge - Day 3 Medium (Project Euler #36 https://projecteuler.net/problem=36)

'''

def split(word):
    return [char for char in word]

def palindrome(list):
    for i in range (0,len(list)//2):
        if list[i] != list[len(list)-i-1]:
            return False
    return True

def palcheck(s):
    return palindrome(split(s))

psum = 0
for i in range(1,1000000):
    if palcheck(str(i)):
        if palcheck(str(bin(i))[2:]):
            psum += i

print(psum)

#Answer: 872187