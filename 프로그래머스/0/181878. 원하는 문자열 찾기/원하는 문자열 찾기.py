def solution(myString, pat):
    answer = 0
    so=''
    for i in str(myString):
        so+=i.lower()
    
    if pat.lower() in so:
        return 1
    else:
        return 0
