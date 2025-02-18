from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0  # 전체 시간
    bridge = deque([0] * bridge_length)  # 다리 위 트럭의 무게를 추적 (0은 빈 공간)
    current_weight = 0  # 다리 위의 현재 무게 합
    
    while truck_weights:  # 트럭이 모두 지나갈 때까지
        time += 1
        # 다리에서 트럭 하나가 나감
        current_weight -= bridge.popleft()
        
        if truck_weights[0] + current_weight <= weight:
            # 트럭이 다리 위에 올라갈 수 있는 경우
            truck = truck_weights.pop(0)
            bridge.append(truck)
            current_weight += truck
        else:
            # 트럭이 다리 위에 올라갈 수 없는 경우, 0을 추가하여 시간을 흐르게 함
            bridge.append(0)
    
    # 마지막 트럭이 다리 끝까지 지나가는데 걸리는 시간
    return time + bridge_length

