from itertools import product

def solution(word):
    answer =0
    num=1
    alpha=['A','E','I','O','U']
    dictionary=[]

    for i in range(5):
        for order in product(alpha,repeat=num):
            dictionary.append(''.join(order))
        num+=1
    
    dictionary.sort()
    answer=dictionary.index(word)+1

    return answer