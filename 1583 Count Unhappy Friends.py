class Solution:
    # find the paired number
    def find_pair_num(self, pairs, num):
        for (a,b) in pairs:
            if a == num:
                return b
            elif b == num:
                return a
        return -1
    
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        mat = [n*[-1] for i in range(n)]
        # create a matrix, which matrix[i][j] denote the preference of i to j
        for i in range(n):
            pref = (preferences[i])
            for k in pref:
                mat[i][k] = n-pref.index(k)

        unhappy = set()
        for (a,b) in pairs:
            idx_a = mat[a][b]
            idx_b = mat[b][a]
            for i in range(n):
                pair_num = self.find_pair_num(pairs, i)
                # if there exists a better pairing, unhappy += 1
                if (mat[a][i] >= idx_a) and (mat[i][a] >= mat[i][pair_num]) and (b != i):
                    print(a, i)
                    unhappy.add(a)
                if (mat[b][i] >= idx_b) and (mat[i][b] >= mat[i][pair_num]) and (a != i):
                    print(b,i)
                    unhappy.add(b)
                   
                
        return len(unhappy)    
