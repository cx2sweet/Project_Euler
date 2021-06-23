"""
A googol (10^100) is a massive number: one followed by one-hundred zeros; 
100100 is almost unimaginably large: one followed by two-hundred zeros. 
Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, a^b, where a, b < 100, 
what is the maximum digital sum?
"""

a=10
b=100
c=a**b
c = list(str(c))
c = [int(num) for num in c]
s = sum(c)

#%%
max_a = 0
max_b = 0
max_pow = 0
max_s = 0
for a in range(100):
    for b in range(100):
        c=a**b
        c = list(str(c))
        c = [int(num) for num in c]
        s = sum(c)
        if s > max_s:
            max_a = a
            max_b = b
            max_pow = a**b
            max_s = s
print(max_s)
#Answer 972