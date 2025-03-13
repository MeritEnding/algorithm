from itertools import product

def solution(word):
    answer = 0
    dictionary=[]

    alpha=['A','E','I','O','U']
    num=1
    for i in range(5):
        for p in product(alpha, repeat=num):
            dictionary.append(''.join(p))
        num+=1
    dictionary.sort()
    answer =dictionary.index(word)+1

    return answer