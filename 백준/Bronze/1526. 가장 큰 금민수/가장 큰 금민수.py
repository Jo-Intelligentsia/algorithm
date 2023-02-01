N = int(input())
gold = [4,7]
for i in range(N,0,-1):
    if all([(s == '4' or s == '7') for s in str(i)]):
        print(i)
        break