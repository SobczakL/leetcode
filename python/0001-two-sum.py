class Solution(object):
    def twoSum(self, nums, target):

        indexes = []

        for i, num1 in enumerate(nums):
            for j, num2 in enumerate(nums):
                if i != j and num1 + num2 == target:
                    indexes.append(i)
                    indexes.append(j)
                    return indexes

        return indexes
