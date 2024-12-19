class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        result = str(x)==str(x)[::-1]
        return result

solution = Solution()
print(solution.isPalindrome(121))