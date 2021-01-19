class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        workers_assigned=[False]*len(workers)
        bikes_assigned=[False]*len(bikes)
        res=[0]*len(workers)
        workers_bikes_assigned=collections.defaultdict(list)
        for i in range(len(workers)):
            for j in range(len(bikes)):
                workers_bikes_assigned[abs(bikes[j][0]-workers[i][0])+abs(bikes[j][1]-workers[i][1])].append([i,j])
        for dist in sorted(workers_bikes_assigned):
            for worker,bike in workers_bikes_assigned[dist]:
                if not workers_assigned[worker] and not bikes_assigned[bike]:
                    workers_assigned[worker]=True
                    bikes_assigned[bike]=True
                    res[worker]=bike
        return res
                    
            
                
                
        
            
                
                
