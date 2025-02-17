def solution(strArr):
    answer =0
    ans =[0]*31
    for i in strArr:
        ans[len(i)] +=1
    
    return max(ans)