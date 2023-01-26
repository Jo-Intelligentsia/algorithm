N = int(input())

ls1 = list(range(1,N+1))
ls2 = []
while len(ls1) >1:
    ls2.append(ls1.pop(0))
    ls1.append(ls1.pop(0))
print(*ls2,ls1[0])