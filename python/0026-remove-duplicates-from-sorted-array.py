class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        count = 1
        j = 1

        while j < len(nums):
            if nums[j] != nums[j - 1]:
                nums[count] = nums[j]
            #update pntrs
                count += 1
            j += 1

        return count
        
