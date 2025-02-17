def solution(s):
    answer = 0
    ans=[]
    s= s.split(' ')
    for i in s:
        if i !='Z':
            ans.append(int(i))
        else:
            ans.pop()
        
    answer= sum(ans)
    
    return answer