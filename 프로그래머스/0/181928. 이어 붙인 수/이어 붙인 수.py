def solution(num_list):
    answer = 0
    j_sum=''
    h_sum=''
    for i in num_list:
        if i%2 ==0:
            j_sum+=str(i)
        else:
            h_sum+=str(i)
    answer =int(j_sum)+int(h_sum)    
    return answer