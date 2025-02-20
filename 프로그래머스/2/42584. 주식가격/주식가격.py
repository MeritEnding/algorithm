from collections import deque
def solution(prices):
    queue= deque(prices)
    answer =[]
    while queue:
        cur_price=queue.popleft()
        time=0
        for p in queue:
            time+=1
            if cur_price > p:
                break
        answer.append(time)
    return answer
    