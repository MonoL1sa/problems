# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """




#solution = Solution()
#print(solution.addTwoNumbers([2,4,3], [5,6,4]))
l1 = [2,4,3]
l2 = [5,6,4]
l3 = l1[::-1] + l2[::-1]

print(l3)
