def solution(num_list):
    answer = []
    j_num=0
    h_num=0
    for i in num_list:
        if i % 2==0:
            j_num +=1
        else:
            h_num +=1
    answer.append(j_num)
    answer.append(h_num)
    return answer