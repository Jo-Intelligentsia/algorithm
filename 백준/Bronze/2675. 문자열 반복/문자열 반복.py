S = int(input())
for i in range(S):
    n ,m = input().split()
    for k in m:
        new = k * int(n)
        print(new,end="")
    print()