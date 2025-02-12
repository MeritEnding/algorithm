def solution(numbers, target):
    answer = 0
    leaves = [0]  # 초기값 0에서 시작
    for num in numbers:
        tmp = []
        for parent in leaves:  # 올바른 변수명 사용
            tmp.append(parent + num)
            tmp.append(parent - num)
        leaves = tmp  # "leves"가 아닌 "leaves" 사용
    for leaf in leaves:
        if leaf == target:
            answer += 1
    return answer
