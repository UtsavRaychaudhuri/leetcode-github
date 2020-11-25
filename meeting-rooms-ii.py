import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if len(intervals)==0:
            return 0
        intervals.sort()
        heap=[intervals[0][1]]
        heapq.heapify(heap)
        for i in range(1,len(intervals)):
            if intervals[i][0]<heap[0]:
                heapq.heappush(heap,intervals[i][1])
            else:
                heapq.heappushpop(heap,intervals[i][1])
        return len(heap)
                
                
        
