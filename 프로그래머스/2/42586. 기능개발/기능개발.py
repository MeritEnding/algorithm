from collections import deque
import math
def solution(progresses, speeds):
    answer = []
    progresses = deque(progresses)
    speeds = deque(speeds)
    
    while progresses:
        day = math.ceil((100- progresses[0])/speeds[0])
        
        for i in range(len(progresses)):
            progresses[i] += day*speeds[i]
        
        release=0
        while progresses and progresses[0]>=100:
            progresses.popleft()
            speeds.popleft()
            release+=1
            
        answer.append(release)
    return answer
        
        
    
    return answer