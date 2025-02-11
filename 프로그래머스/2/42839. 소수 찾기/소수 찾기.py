import math
from itertools import permutations

def is_prime(n):
    if n<=1:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n% i ==0:
            return False
    return True

def solution(numbers):
    unique_numbers= set()

    for i in range(1, len(numbers)+1):
        perms= permutations(numbers,i)
        for perm in perms:
            num =int(''.join(perm))
            unique_numbers.add(num)

    prime_count =sum(1 for num in unique_numbers if is_prime(num))

    return prime_count
