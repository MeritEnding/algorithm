def solution(myString, pat):
    answer = 0
    for i in range(len(myString)):
        if str(myString[i:i+len(pat)]) == str(pat):
            answer+=1
        else:
            continue
            
            
    return answer