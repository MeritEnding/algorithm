def solution(number, k):
    stack = []  # 빈 스택을 만들어서 나중에 숫자를 쌓아갈 예정입니다.
    for n in number:  # number 문자열의 각 문자를 n으로 하나씩 반복합니다.
        # 조건: 스택에 쌓인 숫자가 있고, 제거할 숫자 k가 남아 있으며,
        # 스택의 마지막 숫자가 현재 숫자보다 작을 경우에만 스택에서 숫자를 빼고 k를 감소시킵니다.
        while len(stack) > 0 and k > 0 and stack[-1] < n:
            stack.pop()  # 스택에서 마지막 숫자를 제거합니다.
            k -= 1  # 제거한 숫자만큼 k를 감소시킵니다.
        stack.append(n)  # 현재 숫자 n을 스택에 추가합니다.

    if k:  # 만약 k가 아직 남아 있다면, 즉 제거할 숫자가 남아 있다면
        return number[:-k]  # number에서 뒤에서부터 k개를 제거한 문자열을 반환합니다.
    else:
        return "".join(stack)  # 스택에 쌓인 숫자들을 문자열로 이어서 반환합니다.
