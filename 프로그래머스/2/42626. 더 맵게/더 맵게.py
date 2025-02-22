import heapq
def solution(scoville, K):
    heapq.heapify(scoville)
    c=0
    while True:
        if scoville[0]>=K:
            return c
        elif scoville[0]<K and len(scoville)==1:
            return -1
        else:
            a =heapq.heappop(scoville)+2*heapq.heappop(scoville)
            heapq.heappush(scoville,a)
            c+=1