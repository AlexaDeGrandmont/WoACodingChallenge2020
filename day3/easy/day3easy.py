'''
CCSS WoA Coding Challenge - Day 3 Easy (Project Euler #4 https://projecteuler.net/problem=4)

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

prodlist = []
for i in range (100,1000):
    for j in range(100,1000):
        product = i*j
        if palcheck(str(product)):
            prodlist.append(product)

mx = 0
for i in prodlist:
    if i > mx:
        mx = i
print(mx)

#Answer: 906609