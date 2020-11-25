import heapq
class MedianFinder(object):
​
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_heap=[]
        self.max_heap=[]
        
​
    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        heapq.heappush(self.max_heap,-num)
        heapq.heappush(self.min_heap,-heapq.heappop(self.max_heap))
        if len(self.min_heap)>len(self.max_heap):
            heapq.heappush(self.max_heap,-heapq.heappop(self.min_heap))
        
        
        
​
    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.min_heap)==len(self.max_heap):
            return 0.5*(self.min_heap[0]+-self.max_heap[0])
        else:
            return -self.max_heap[0]
        
        
​
​
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
