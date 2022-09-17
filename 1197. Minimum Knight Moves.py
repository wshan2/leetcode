class Solution:
# DFS with memoization 

    @lru_cache(maxsize=None)
    def dfs(self, x, y):
        if x+y == 0:
            return 0
        elif x+y == 2:
            return 2
        else:
            return min(self.dfs(abs(x-1), abs(y-2)), self.dfs(abs(x-2), abs(y-1))) + 1 
        
    
    def minKnightMoves(self, x: int, y: int) -> int:
        return self.dfs(abs(x), abs(y))
        
    
class Solution:
   # BFS with time limit exceeded (TLE lol)
    def bfs(self,x,y):
        offsets = [(1, 2), (2, 1), (2, -1), (1, -2),
                   (-1, -2), (-2, -1), (-2, 1), (-1, 2)]
        visited = set()
        queue = deque([(0,0)])
        steps = 0
        
        while queue:
            curr_level_cnt = len(queue)
            for i in range(curr_level_cnt):
                curr_x, curr_y = queue.popleft()
                if (curr_x, curr_y) == (x,y):
                    return steps
                
                for offset_x, offset_y in offsets:
                    next_x, next_y = curr_x + offset_x, curr_y + offset_y
                    if (next_x, next_y) not in visited:
                        visited.add((next_x, next_y))
                        queue.append((next_x, next_y))
        
            steps += 1
            
    def minKnightMoves(self, x: int, y: int) -> int:
        return self.bfs(x,y)
