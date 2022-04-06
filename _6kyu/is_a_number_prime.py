"""Description:
Define a function that takes one integer argument and returns logical value true or false depending on if the integer
is a prime.

Per Wikipedia, a prime number (or a prime) is a natural number greater than 1 that has no positive divisors other than
1 and itself.

Requirements
You can assume you will be given an integer input.
You can not assume that the integer will be only positive. You may be given negative numbers as well (or 0).
NOTE on performance: There are no fancy optimizations required, but still the most trivial solutions might time out.
Numbers go up to 2^31. Looping all the way up to n, or n/2, will be too slow"""


import math


def is_prime(num):
    if num < 2:
        return False
    a = 2
    while a <= math.sqrt(num):
        if num % a < 1:
            return False
        a += 1
    return True


print(is_prime(0))
print(is_prime(1))
print(is_prime(2))
print(is_prime(73))
print(is_prime(75))
print(is_prime(-1))
