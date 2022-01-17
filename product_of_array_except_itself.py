from sys import prefix


class Solution:
    def productExceptSelf(self, nums):
        prefixs = [1]
        suffixs = [1]*len(nums)
   
        for i in range(1,len(nums)):
            prefixs.append(prefixs[-1]*nums[i-1])

        for i in range(len(nums)-1,0,-1):
            suffixs[i-1] = nums[i]*suffixs[i]

        results = []
        for i in range(len(nums)):
            results.append(prefixs[i]*suffixs[i])

        return results

    # optimized only space
    def productExceptSelfOptimized(self, nums):
        result = [1]*(len(nums))
       
        prefix =  1
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums)-1,-1,-1): 
            result[i] *= postfix
            postfix *=  nums[i]
        
        return result
         


sol = Solution()

print(sol.productExceptSelf([1,2,3,4]))
        