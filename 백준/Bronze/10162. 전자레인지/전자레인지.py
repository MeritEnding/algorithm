t= int(input())

array= [300,60,10]
score=[0,0,0]

if t%10!=0:
    print(-1)
else:
    for i in range(3):
        if t>=array[i]:
            score[i]= t //array[i]
            t %= array[i]

    for i in score:
        print(i, end=' ')
            
