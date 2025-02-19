def solution(participant, completion):
    hashDict={}
    sum=0
    for part in participant:
        hashDict[hash(part)]=part
        sum+=hash(part)
    
    for comp in completion:
        sum-=hash(comp)
    
    return hashDict[sum]
