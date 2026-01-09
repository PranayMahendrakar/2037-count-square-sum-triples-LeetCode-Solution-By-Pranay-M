class Solution:
    def countTriples(self, n: int) -> int:
        count = 0
        squares = set(i*i for i in range(1, n+1))
        
        for a in range(1, n+1):
            for b in range(1, n+1):
                c_sq = a*a + b*b
                if c_sq in squares:
                    count += 1
        
        return count