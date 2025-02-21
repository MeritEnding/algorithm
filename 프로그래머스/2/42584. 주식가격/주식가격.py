from collections import deque
def solution(prices):
    answer = []
    prices_q = deque(prices)
    
    while prices_q:
        cur_price = prices_q.popleft()
        time = 0
        for p in prices_q:
            time += 1
            if cur_price > p:
                break
        answer.append(time)
        
    return answer
    
    return answer