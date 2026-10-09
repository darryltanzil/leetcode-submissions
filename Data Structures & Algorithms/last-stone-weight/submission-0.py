import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """
        create a maxHeap, pop two from the top
        """
        maxHeap = stones
        heapq.heapify_max(maxHeap)

        while len(maxHeap) > 1:
            x, y = heapq.heappop_max(maxHeap), heapq.heappop_max(maxHeap)
            if x < y: 
                heapq.heappush_max(maxHeap, y - x)
            else:
                heapq.heappush_max(maxHeap, x - y)
        
        return maxHeap[0]