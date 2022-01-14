class Solution:
    def containsDuplicate(self, nums):
        nums_dict = {}
        for i in range(len(nums)):
            if nums[i] in nums_dict.keys():
                nums_dict[nums[i]] =  nums_dict[nums[i]]+1
                return True
            else:
                nums_dict[nums[i]] = 1
                
        return False


