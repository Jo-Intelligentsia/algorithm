N = int(input())
a = []
queue = [i for i in range(1,N+1)]

while len(queue) > 1:
    a.append(queue.pop(0))
    queue.append(queue.pop(0))
print(*a,queue[0])
