def solution(myString):
    answer = ''
    st=''
    for i in myString:
        if i =='a' or i =='A':
            st= i.upper()
            answer+=st
        else:
            st= i.lower()
            answer+=st
        
    return answer