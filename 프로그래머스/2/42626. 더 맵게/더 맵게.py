import heapq
def solution(scovile, K):

    heapq.heapify(scovile)
    c =0

    while True:
        if scovile[0]>=K:
            return c
        elif scovile[0] <K and len(scovile)==1:
            return -1
        else:
            a =heapq.heappop(scovile) +(heapq.heappop(scovile)*2)
            heapq.heappush(scovile,a)
            c+=1