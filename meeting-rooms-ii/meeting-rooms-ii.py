class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        l=[[intervals[0][1],intervals[0][0]]]
        heapq.heapify(l)
        for i,j in intervals[1:]:
            if i<l[0][0]:
                heapq.heappush(l,[j,i])
            else:
                heapq.heappushpop(l,[j,i])
        return len(l)
            