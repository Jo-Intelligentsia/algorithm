import heapq

N = list(map(int,input().split()))
heapq.heapify(N)
heapq.heappop(N)
print(N[0])