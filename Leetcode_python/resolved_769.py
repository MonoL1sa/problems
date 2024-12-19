from typing import List
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        max_value = 0
        c = 0
        
        for i in range(len(arr)):
            max_value = max(max_value, arr[i])
            if max_value == i:
                c += 1
        
        return c
solution = Solution()
print(solution.maxChunksToSorted([4,3,2,1,0]))