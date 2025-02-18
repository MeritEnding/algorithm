from collections import deque
def solution(priorities, location):
    queue =deque()

    for i in range(len(priorities)):
        queue.append((priorities[i],i))

    answer =0

    while queue:
        cursor= queue.popleft()
        max_priority =max([i[0] for i in queue],default=0)
        if cursor[0] < max_priority:
            queue.append(cursor)
        else:
            answer+=1
            if cursor[1]==location:
                return answer