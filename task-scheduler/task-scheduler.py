class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        tasks_map=collections.defaultdict(int)
        max_freq=0
        maxcount=0
        for t in tasks:
            tasks_map[t]+=1
            max_freq=max(max_freq,tasks_map[t])
        for i in tasks_map:
            if tasks_map[i]==max_freq:
                maxcount+=1
        partitions=max_freq-1
        empty=partitions*(n-maxcount+1)
        pending=len(tasks)-max_freq*maxcount
        idle=max(0,empty-pending)
        return len(tasks)+idle
            
        
