from collections import deque
def solution(priorities, location):

    queue= deque()

    for i in range(len(priorities)):
        queue.append((priorities[i],i))
    answer=0
    
    while queue:
        cur=queue.popleft()
        max_value = max([i[0] for i in queue],default=0)

        if cur[0] < max_value:
            queue.append(cur)
        else:
            answer+=1
            if cur[1]==location:
                return answer
