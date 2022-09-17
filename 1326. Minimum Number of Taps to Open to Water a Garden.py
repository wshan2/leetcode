class Solution:
 # time complexity O(n), space complexity O(n)
    def minTaps(self, n: int, ranges: List[int]) -> int:
        maxRange = [0]*(n+1)
        for i, r in enumerate(ranges):
            left = max(0, i-r)
            right = min(n, i+r)
            maxRange[left] = right-left
            
        left = right = farthest = taps = 0
        while right < n:
            for i in range(left, right+1):
                farthest = max(farthest, i+maxRange[i])
            left = right
            right = farthest
            if left == right:
                return -1
            taps += 1
        return taps
