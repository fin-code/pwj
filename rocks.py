from typing import List
import heapq

def lastStoneWeight( stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        #max heap
        stones =[-x for x in stones]
        heapq.heapify(stones)
        #print(stones)
        #x = -heapq.heappop(stones)
        result = -1
        while len(stones) > 1:
         #   print('current heap', stones)
                y = -heapq.heappop(stones)
                x = -heapq.heappop(stones)
                #print(y,x)
                y -= x
                #print('total: ',y)
                if y > 0:
                    heapq.heappush(stones,y * -1)
            #print(stones)
        return stones[0]* -1
            


rocks = [1]
rocks2 = [2,7,4,1,8,1]

print('result:     ',lastStoneWeight(rocks2))