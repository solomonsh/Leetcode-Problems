class Solution:
    def climbStairs(self, n: int) -> int:
        
        first = 0
        second = 0

        for i in range(n-1):
            temp = first
            first = first + second
            second = temp

        return first



     