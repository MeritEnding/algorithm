def solution(arr, n):
    answer = []
    
    if len(arr)%2 !=0:
        for idx, value in enumerate(arr):
            if idx %2==0:
                answer.append(value+n)
            else:
                answer.append(value)
    else:
        for idx, value in enumerate(arr):
            if idx %2 !=0:
                answer.append(value+n)
            else:
                answer.append(value)
        
    return answer