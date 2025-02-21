from collections import deque
def solution(prices):
    answer = []
    price_q = deque(prices)
    
    while price_q:
        cur = price_q.popleft()
        time = 0    
        for p in price_q:
            time+=1
            if cur > p:
                break
        answer.append(time)
        
    return answer