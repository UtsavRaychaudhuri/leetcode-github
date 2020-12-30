class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        snakes_and_ladders_arr=[0]
        reverse=False
        for i in reversed(board):
            if reverse:
                for j in reversed(i):
                    snakes_and_ladders_arr.append(j)
                reverse=False
                continue
            for j in i:
                snakes_and_ladders_arr.append(j)
            reverse=True
        q=collections.deque([1])
        seen=set()
        moves=0
        while(q):
            size=len(q)
            for i in range(size):
                ele=q.popleft()
                for i in range(1,7):
                    if ele+i==len(board)*len(board) or snakes_and_ladders_arr[ele+i]==len(board)*len(board):
                        return moves+1
                    if ele+i<len(board)*len(board) and snakes_and_ladders_arr[ele+i]==-1 and ele+i not in seen:
                        q.append(ele+i)
                        seen.add(ele+i)
                    elif ele+i<len(board)*len(board) and snakes_and_ladders_arr[ele+i] not in seen:
                        q.append(snakes_and_ladders_arr[ele+i])
                        seen.add(snakes_and_ladders_arr[ele+i])
            moves+=1
        return -1
                        
