from collections import deque
def solution(prices):
    price_q =deque(prices)
    answer =[]
    while price_q:
        cur_price =price_q.popleft()
        time=0    
        for p in price_q:
            time+=1
            if cur_price >p:
                break
        answer.append(time)
    return answer
    