class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes=sorted(envelopes,key=lambda envelope:(envelope[0],-envelope[1]))
        nums=[]
        for i in envelopes:
            nums.append(i[1])
            
        if len(envelopes)==0:
            return 0
        bs_array=[envelopes[0][1]]
        def bs(bs_array,element):
            low=0
            hi=len(bs_array)-1
            while(low<=hi):
                mid=low+hi>>1
                if bs_array[mid]==element:
                    return mid
                if bs_array[mid]>element:
                    hi=mid-1
                else:
                    low=mid+1
            return low
        for i in range(1,len(nums)):
            if nums[i]<bs_array[-1]:
                idx=bs(bs_array,nums[i])
                bs_array[idx]=nums[i]
            elif bs_array[-1]!=nums[i]:
                bs_array.append(nums[i])
        return len(bs_array)
    
                
                
        
        
