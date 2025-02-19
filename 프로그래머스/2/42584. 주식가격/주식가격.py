from collections import deque
def solution(prices):
    queue= deque(prices)

    answer =[]

    while queue:
        time =0
        cur_value=queue.popleft()
        for q in queue:
            time+=1
            if cur_value > q:
                break
        answer.append(time)

    return answer