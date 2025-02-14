def solution(my_string, is_suffix):
    answer = 0
    array=[]
    for i in range(0,len(my_string)):
        array.append(my_string[i:])
    if is_suffix in array:
        answer=1
    else:
        answer=0
    
    return answer