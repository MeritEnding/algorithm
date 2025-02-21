def solution(n, lost, reserve):
    net_lost =set(lost)-set(reserve)
    net_reserve=set(reserve)-set(lost)
    
    answer = n- len(net_lost)
    
    for i in sorted(net_lost):
        if i-1 in net_reserve:
            net_reserve.remove(i-1)
            answer+=1
        elif i+1 in net_reserve:
            net_reserve.remove(i+1)
            answer+=1
    return answer