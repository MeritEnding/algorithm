import math
def solution(a, b):
    answer = 0
    if a %2 !=0 and b%2 !=0:
        answer= math.pow(a,2)+math.pow(b,2)
    elif a %2 !=0 or b%2 !=0:
        answer = 2*(a+b)
    else:
        answer =abs(a-b)
    return answer