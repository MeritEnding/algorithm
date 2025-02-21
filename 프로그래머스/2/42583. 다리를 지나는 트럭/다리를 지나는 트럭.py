from collections import deque
def solution(bridge_length, weight, truck_weights):
    bridge = deque([0]*bridge_length)
    current_weight=0
    time = 0
    
    while truck_weights:
        current_weight-= bridge.popleft()
        
        time+=1
        
        if current_weight + truck_weights[0]<=weight:
            truck= truck_weights.pop(0)
            bridge.append(truck)
            current_weight+=truck
        else:
            bridge.append(0)
            
    return time + bridge_length
            