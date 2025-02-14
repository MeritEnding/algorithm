def solution(num_list):
    answer = 0
    h_sum=0
    j_sum=0
    for i in range(len(num_list)):
        if i % 2 !=0:
            h_sum +=num_list[i]
        else:
            j_sum +=num_list[i]
            
    if h_sum >j_sum:
        answer=h_sum
    elif h_sum< j_sum:
        answer=j_sum
    else:
        answer= h_sum
        
    return answer