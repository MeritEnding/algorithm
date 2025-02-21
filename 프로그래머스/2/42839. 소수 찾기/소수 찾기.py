from itertools import permutations
import math
def is_prime(n):
    if n<=1:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i ==0:
            return False
    return True

def solution(numbers):
    answer = 0
    unique = set()
    for i in range(1,len(numbers)+1):
        perms = permutations(numbers, i)
        for perm in perms:
            num = int(''.join(perm))
            unique.add(num)
            
    prime_count = sum(1 for i in unique if is_prime(i))
    
    return prime_count
        
    
    
    
    return answer