'''
CCSS WoA Coding Challenge - Day 3 Hard (Project Euler #162 https://projecteuler.net/problem=36)

'''

#formula = 15*16**(n-1) - 43*15**(n-1) + 41*14**(n-1) - 13**n

def resultUpTo(n):
    hsum = 0
    for i in range(3,n+1):
        hsum += (15*16**(i-1) - 43*15**(i-1) + 41*14**(i-1) - 13**i)
    return hsum
    
print(hex(resultUpTo(16)))