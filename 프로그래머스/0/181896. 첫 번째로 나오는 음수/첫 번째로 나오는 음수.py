def solution(num_list):
    answer = len(num_list)
    count=0
    for idx, value in enumerate(num_list):
        if value < 0:
            answer=min(answer,idx)
            count+=1
    if count ==0:
        return -1
    else:        
        return answer