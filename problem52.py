"""
It can be seen that the number, 125874, and its double, 251748, 
contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, 
contain the same digits.
"""

def split(n):
    digs = []
    while n >=10:
        digs.append(n%10)
        n = n//10
    digs.append(n)
    
    return digs
    
#%%
#125874
for i in range(1,1000000):
    a = set(split(i))
    if a == set(split(i*2)):
        if a == set(split(i*3)):
            if a == set(split(i*4)):
                if a == set(split(i*5)):
                    if a == set(split(i*6)):
                        print(i)

#142857