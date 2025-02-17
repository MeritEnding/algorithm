def solution(s):
    answer = ''
    result =[]
    
    for i in range(len(s)):
        count=0
        for j in range(len(s)):
            if s[i] == s[j]:
                count+=1
        if count-1 >0:
            continue
        else:
            result.append(s[i])
    result =sorted(result)    
        
    return ''.join(result)