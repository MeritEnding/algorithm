from collections import deque
import math
def solution(progresses, speeds):
    answer =[]
    progresses =deque(progresses)
    speeds =deque(speeds)

    while progresses:
        # 현재 첫번째 작업이 완료될 때까지 필요한 일 수 계산
        days=math.ceil((100-progresses[0])/speeds[0])

        # 모든 작업을 days일 만큼 진행
        for i in range(len(progresses)):
            progresses[i]+=speeds[i]*days
        
        # 배포할 수 있는 작업 개수확인
        release =0

        while progresses and progresses[0]>=100:
            release+=1
            progresses.popleft()
            speeds.popleft()
        answer.append(release)

    return answer