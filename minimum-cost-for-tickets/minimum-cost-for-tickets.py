class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        @lru_cache(maxsize=None)
        def mct(i,curr):
            cost1=cost2=sys.maxsize
            while(i<len(days) and days[i]<curr):
                i+=1
            if i==len(days):
                return 0
            cost0=costs[0]+mct(i+1,days[i]+1)
            while(i<len(days) and days[i]<curr):
                i+=1
            if i==len(days):
                return 0
            cost1=costs[1]+mct(i+1,days[i]+7)
            while(i<len(days) and days[i]<curr):
                i+=1
            if i==len(days):
                return 0
            cost2=costs[2]+mct(i+1,days[i]+30) 
            return min(cost0,cost1,cost2)
        return mct(0,days[0])