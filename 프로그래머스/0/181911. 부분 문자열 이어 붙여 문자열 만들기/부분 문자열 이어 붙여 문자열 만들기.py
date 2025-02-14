def solution(my_strings, parts):
    answer = ''
    for i in range(len(my_strings)):
        s,e = parts[i]
        sample=my_strings[i]
        answer+= sample[s:e+1]
    return answer