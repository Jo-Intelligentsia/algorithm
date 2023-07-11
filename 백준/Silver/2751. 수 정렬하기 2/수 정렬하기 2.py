import sys
input = sys.stdin.readline

N = int(input())
k = []
for i in range(N):
    n = int(input())
    k.append(n)

k.sort()
for i in k:
    print(i)