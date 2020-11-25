import heapq
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        missingpositive=1
        heapq.heapify(nums)
        while(nums):
            num = heapq.heappop(nums)
            if num==missingpositive:
                missingpositive+=1
            if num>=missingpositive+1:
                return missingpositive
        return missingpositive
        
