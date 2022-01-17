class Solution:
    def maxProduct(self, nums):
        
      
        curr_minimum = 1
        curr_maximum = 1

        result = max(nums)
        
        for n in nums:
            
            temp =  curr_maximum * n

            curr_maximum = max(n,n*curr_minimum,n*curr_maximum)
            curr_minimum = min(n,n*curr_minimum,temp)

            result = max(result,curr_maximum)      

        return result

