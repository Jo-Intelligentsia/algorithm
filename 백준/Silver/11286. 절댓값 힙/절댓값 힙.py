import heapq
import sys

T = int(sys.stdin.readline())
heap = []
heapq.heapify(heap)
for i in range(T):
    n = int(sys.stdin.readline())
    if abs(n) != 0:
        heapq.heappush(heap,(abs(n),n))
    elif abs(n) == 0:
        if heap:
            a = heapq.heappop(heap)
            print(a[1])
            
        else:
            print('0')
