from collections import deque
import math
def solution(progresses, speeds):
    progresses=deque(progresses)
    speeds=deque(speeds)
    answer =[]
    
    while progresses:
        day= math.ceil((100-progresses[0])/speeds[0])
        
        for i in range(len(progresses)):
            progresses[i]+=day*speeds[i]
        
        release=0
        while progresses and progresses[0]>=100:
            release+=1
            progresses.popleft()
            speeds.popleft()
        answer.append(release)
        
    return answer