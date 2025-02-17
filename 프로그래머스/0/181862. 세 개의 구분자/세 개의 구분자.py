def solution(myStr):
    answer = []
    i=0
    ans=''
    for i in str(myStr):
        if i!='a' and i!='b' and i!='c':
            ans+= str(i)
        else:
            if ans:
                answer.append(ans)
                ans=''
            else:
                continue
    if ans:
        answer.append(ans)
    
    if len(answer)==0:
        answer.append("EMPTY")

    return answer