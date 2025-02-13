a=[]

for i in range(9):
    a.append(int(input()))

for j in range(9):
    b =a[j]

    for k in range(j+1,9):
        c= a[k]
        if sum(a)-b-c ==100:
            a.remove(b)
            a.remove(c)
            break
    if sum(a) ==100:
        break

a.sort()

for n in a:
    print(n)