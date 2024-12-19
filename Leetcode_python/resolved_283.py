from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        position = 0
        for num in nums:
            if num != 0:
                nums[position] = num
                position += 1
        for i in range(position, len(nums)):
            nums[i] = 0
            
nums = [0, 1, 0, 3, 12]
solution = Solution()
solution.moveZeroes(nums)
print(nums)