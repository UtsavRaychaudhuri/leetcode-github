class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        my_set=set()
        final_set=set()
        count=0
        for i in nums:
            if i+k in my_set:
                if i>i+k:
                    final_set.add((i+k,i))
                else:
                    final_set.add((i,i+k))
            if i-k in my_set:
                if i>i-k:
                    final_set.add((i-k,i))
                else:
                    final_set.add((i-k,i))
            my_set.add(i)
        return len(final_set)