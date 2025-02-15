def solution(numbers, direction):
    answer = []
    if direction =="right":
        for i in range(len(numbers)):
            if i == 0:
                answer.append(numbers[-1])
            else:
                answer.append(numbers[i-1])
    else:
        for j in range(len(numbers)):
            if j == len(numbers)-1:
                answer.append(numbers[0])
            else:
                answer.append(numbers[j+1])
                
    return answer