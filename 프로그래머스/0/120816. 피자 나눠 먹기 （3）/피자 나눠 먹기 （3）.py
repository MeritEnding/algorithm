import math
def solution(slice, n):
    answer = 0
    if slice >=n:
        answer = 1
    else:
        answer= math.ceil(n/slice)
        
    return answer