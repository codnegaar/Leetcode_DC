class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        
        heap = []        
        for index in range(len(heights) - 1):
            
            diff = (heights[index+1] - heights[index])
            if diff > 0:
                heappush(heap, diff)            
            if len(heap) > ladders:
                bricks -= heappop(heap)
            if bricks < 0:
                return index
        return len(heigths) -1
                
