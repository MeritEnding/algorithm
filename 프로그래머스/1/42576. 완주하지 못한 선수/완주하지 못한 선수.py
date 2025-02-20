def solution(participant, completion):
    hash_map={}
    sum=0
    for part in participant:
        hash_map[hash(part)]=part
        sum+=hash(part)
    for comp in completion:
        sum-=hash(comp)
    
    return hash_map[sum]