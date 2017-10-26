class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_dict = {}
        for index in range(len(nums)):
            if nums[index] in nums_dict:
                return [nums_dict[nums[index]], index]
            else:
                nums_dict[target - nums[index]] = index
