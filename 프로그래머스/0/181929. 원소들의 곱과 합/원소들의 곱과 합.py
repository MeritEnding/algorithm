import math
def solution(num_list):
    answer = 0
    a= sum(num_list)
    if math.prod(num_list)< math.pow(a,2):
        return 1
    else:
        return 0
    return answer