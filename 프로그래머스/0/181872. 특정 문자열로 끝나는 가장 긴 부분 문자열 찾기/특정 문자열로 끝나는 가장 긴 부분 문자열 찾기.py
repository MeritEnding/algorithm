def solution(myString, pat):
    answer = ''
    i=0
    for i in range(len(myString)):
        if myString[i:i+len(pat)]==pat:
            answer =myString[0: i+len(pat)]
    return answer