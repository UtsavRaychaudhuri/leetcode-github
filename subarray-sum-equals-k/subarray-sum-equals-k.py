class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        rsum={0:1}
        count=0
        running_sum=0
        for i in nums:
            running_sum+=i
            if running_sum-k in rsum:
                count+=rsum[running_sum-k]
            if running_sum in rsum:
                rsum[running_sum]+=1
            else:
                rsum[running_sum]=1
        return count