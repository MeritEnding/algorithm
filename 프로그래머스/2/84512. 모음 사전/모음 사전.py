from itertools import product
def solution(word):

    num =1
    answer=0
    dictionary=[]

    alpha=['A','E','I','O','U']
    for i in range(5):
        for order in product(alpha, repeat=num):
            dictionary.append(''.join(order))
        num+=1
    dictionary.sort()
    answer =dictionary.index(word)+1

    return answer
   