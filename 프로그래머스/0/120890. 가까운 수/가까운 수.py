def solution(array, n):
    array.sort()  # 정렬하여 가장 가까운 숫자가 여러 개일 경우 작은 수가 먼저 오도록 함
    answer = array[0]
    min_diff = abs(n - answer)
    
    for num in array:
        diff = abs(n - num)
        if diff < min_diff:  # 더 작은 차이가 나타나면 갱신
            min_diff = diff
            answer = num
        elif diff == min_diff and num < answer:  # 차이가 같다면 더 작은 수 선택
            answer = num
    
    return answer
