from math import sqrt
import heapq 
from typing import List

def kClosest( points: List[List[int]], k: int) -> List[List[int]]:
    #heap =[distance and coordinates]
    heap = []
    for p in points:
        heapq.heappush(heap,(sqrt(p[0] ** 2 + p[1] ** 2 ),p))
    result = []
    for _ in range(k):
        _, val = heapq.heappop(heap)
        result.append(val)
    return result

points = [[3,3],[5,-1],[-2,4]]
k = 2

print(kClosest(points,k))