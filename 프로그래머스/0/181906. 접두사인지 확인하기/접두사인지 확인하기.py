def solution(my_string, is_prefix):
    answer = 0
    arr=[]
    for i in range(1,len(my_string)):
        arr.append(my_string[:i])
    if is_prefix in arr:
        answer=1
    else:
        answer=0
    
    return answer