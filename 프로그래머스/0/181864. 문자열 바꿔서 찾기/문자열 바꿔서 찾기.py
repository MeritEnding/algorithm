def solution(myString, pat):
    answer = 0
    st=''
    for i in str(myString):
        if i=='A':
            st+='B'
        elif i=='B':
            st+='A'
    
    if pat in st:
        answer =1
    else:
        answer=0
    return answer