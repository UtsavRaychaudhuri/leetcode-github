class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        my_dict=collections.defaultdict(int)
        maxfreq=0
        for i in nums:
            my_dict[i]+=1
            maxfreq=max(maxfreq,my_dict[i])
        buckets=[0]*(maxfreq+1)
        for i in my_dict:
            if buckets[my_dict[i]]==0:
                buckets[my_dict[i]]=[i]
            else:
                buckets[my_dict[i]].append(i)
        res=[]
        for i in range(len(buckets)-1,-1,-1):
            if buckets[i]==0:
                continue
            if len(res)==k:
                break
            for number in buckets[i]:
                if len(res)==k:
                    break
                res.append(number)
        return res
            
        
        count = collections.Counter(nums)   
        return heapq.nlargest(k, count.keys(), key=count.get)
    
        