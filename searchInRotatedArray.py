class Solution:

    def search(self, nums, target):

        if len(nums) == 1:
            return 0 if nums[0] == target else -1

        start, end = 0, len(nums)-1

        pivot_found = False
        while start <= end:
            median_index = (start+end)//2

            if nums[start] < nums[end]:
                pivot_found = True

            if nums[median_index] == target:
                return median_index

            if pivot_found:
                if nums[median_index] > target:
                    end = median_index-1
                else:
                    start = median_index+1
            else:
                if nums[median_index] > nums[median_index+1]:
                    pivot_found = True
                    if nums[0] <= target:
                        start = 0
                        end = median_index
                    else:
                        start = median_index+1
                        end = len(nums)-1
                if nums[0] <= nums[median_index] and not pivot_found:
                    start = median_index+1
                else:
                    if not pivot_found:
                        end = median_index

        return -1


sol = Solution()


print(sol.search([4], 5))
