# First in, first out
l=[]
l.append(1)
l.append(2)
l.append(3)
l.pop(0)
l.pop(0)
l.pop(0)
# FILO
l=[]
l.append(1)
l.append(2)
l.append(3)
l.pop()
l.pop()
l.pop()
# Priority Queue
from queue import PriorityQueue
pq=PriorityQueue
pq.put(3)
pq.put(100)
pq.put(50)
pq.queue
pq.get()
# Heapq
import heapq
l=[]
heapq.heappush(l,8)
heapq.heappush(l,1)
heapq.heappush(l,5)
heapq.heappush(l,3)
heapq.heappop(l)
# Deque: double-ended queue
from collections import deque
deq=deque()
deq.append(1)
deq.append(2)
deq.append(3)
print(deq.popleft())
print(deq.popleft())
print(deq.popleft())
