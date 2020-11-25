class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict={}
        for i,v in enumerate(nums):
            if target-v in my_dict:
                return [my_dict[target-v],i]
            my_dict[v]=i
                
            
