"""
There are exactly ten ways of selecting three from five, 12345:

123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, (5 C 3) = 10.

It is not until (23 C 10) = 1144066, that a value exceeds one-million: 

How many, not necessarily distinct, values of (n C r)
 for 1 <= n <= 100, are greater than one-million?
 """
 
from math import comb
count = 0
for n in range(101):
    for r in range(n):
        if comb(n,r) >= 1000000: 
            #print(comb(n,r))
            count +=1

print(count)