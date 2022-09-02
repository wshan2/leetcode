class Solution:    
  # Time Complexity: O(n^2), going over n nodes and two for loops with n iterations is O(n(n+n)) = O(n^2)
  # Space Complexity: O(n), using only two arrays of size n
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        mstCost = 0
        edgesUsed = 0
        inMST = [False] * n
        
        min_dist = [math.inf] * n
        min_dist[0] = 0
        
        while edgesUsed != n:
            cur_min_edge = math.inf
            cur_node = -1
            
            # find node with minimum cost to add to the Tree
            for node in range(n):
                if not inMST[node] and cur_min_edge > min_dist[node]:
                    cur_min_edge = min_dist[node]
                    cur_node = node
            
            mstCost += cur_min_edge
            edgesUsed += 1
            inMST[cur_node] = True
            
            # update the min_dist array
            for next_node in range(n):
                weight = abs(points[cur_node][0] - points[next_node][0]) +\
                         abs(points[cur_node][1] - points[next_node][1])
                
                if not inMST[next_node] and min_dist[next_node] > weight:
                    min_dist[next_node] = weight
        
        return mstCost
