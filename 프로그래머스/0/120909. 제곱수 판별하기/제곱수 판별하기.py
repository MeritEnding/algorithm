def solution(n):
    count =0
    arr=[]
    for i in range(n):
        arr.append(i*i)
    
    if n in arr:
        answer=1
    else:
        answer=2
    return answer