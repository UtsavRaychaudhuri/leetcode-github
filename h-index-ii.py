class Solution:
    def hIndex(self, citations: List[int]) -> int:
        left=0
        length = len(citations)
        right= length-1
        while(left<=right):
            
            mid=(left+right)>>1
            if(citations[mid] == (length-mid)):
                return citations[mid]
            elif(citations[mid] > (length-mid)):
                right = mid - 1
            else:
                left = mid + 1
        return length - (right+1)
