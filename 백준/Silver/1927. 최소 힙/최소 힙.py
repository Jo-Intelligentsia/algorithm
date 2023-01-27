import heapq
import sys
N = int(sys.stdin.readline())
heap =[]

for i in range(N):
    x = int(sys.stdin.readline())
    if x != 0:
        heapq.heappush(heap,x)
    else:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)