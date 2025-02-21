from collections import deque
import math
def solution(progresses, speeds):
    answer = []
    progresses = deque(progresses)
    speeds = deque(speeds)
    
    while progresses:
        day = math.ceil((100-progresses[0])/speeds[0])
        
        for i in range(len(progresses)):
            progresses[i] +=speeds[i]*day
            
        release=0
        while progresses and progresses[0]>=100:
            release += 1
            progresses.popleft()
            speeds.popleft()
        answer.append(release)
    return answer
            
        
    return answer