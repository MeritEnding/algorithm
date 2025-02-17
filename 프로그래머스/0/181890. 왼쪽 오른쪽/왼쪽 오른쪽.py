def solution(str_list):
    answer=[]
    for i in range(len(str_list)):
        a=str_list[i]
        if a == "l":
            answer=str_list[:i]
            break
        
        elif a =="r":
            answer=str_list[i+1:]
            break
        
    return answer