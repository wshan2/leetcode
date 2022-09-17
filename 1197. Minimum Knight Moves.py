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
        
    
