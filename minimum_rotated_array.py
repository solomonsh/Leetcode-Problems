class Solution:
    def findMin(self, nums):

        n = len(nums)
    
        start = 0
        end = len(nums)-1
      
        
        while start<end:
            median_index = (start+end)//2
            if nums[median_index] > nums[median_index+1]:
                return nums[median_index+1]

            if nums[0] <= nums[median_index]:
                start = median_index+1 
            else:
                end = median_index
        
        return nums[0]
                



sol = Solution()

print(sol.findMin( [3,1,2]))